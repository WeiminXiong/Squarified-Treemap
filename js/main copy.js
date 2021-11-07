{
  let _width = $(window).width();
  let _height = $(window).height();
  let width = _width;
  let height = _height;

  let data = null;
  let data_file = "./data/data.json";

  let fontFamily;

  function setUi() {
    // 设置字体
    let ua = navigator.userAgent.toLowerCase();
    fontFamily = "楷体";
    if (/\(i[^;]+;( U;)? CPU.+Mac OS X/gi.test(ua)) {
      fontFamily = "PingFangSC-Regular";
    }
    d3.select("body").style("font-family", fontFamily);
  }

  function treemap(data, width, height) {
    // Simple Treemap
    // 输入：数据，画布宽高
    // 输出：叶节点的位置及大小

    // 补充非叶节点的数量信息
    function getValue(node) {
      if (node.children == null || node.children.length == 0) return;
      let value = 0;
      for (let i in node.children) {
        let n = node.children[i];
        getValue(n);
        value += n.value;
      }
      node.value = value;
    }
    getValue(data);

    let square = width * height;
    let sum = data.value;
    
    //将面积等比例缩放
    function change(node) {
      if (node.children == null || node.children.length == 0)
        node.square = node.value / sum * square;
      else {
        for (let i in node.children)
          change(node.children[i]);
        node.square = node.value / sum * square;
      }
    }
    change(data)


    // 计算叶节点位置，判断是否转变方向
    // 保留第一层信息，方便染色
    function calcPos(childlist, rowlist, x, y, width, height, parent, score, leaves) {
    
      //计算平均长宽比
      function worst(R, W) {
        if (R.length == 0)
          return 1e30;
        let rmx = 0;
        let rmn = 1e30;
        let s = 0;
        for (let i = 0; i < R.length; i++) {
          if (R[i].square > rmx)
            rmx = R[i].square;
          if (R[i].square < rmn)
            rmn = R[i].square;
          s += R[i].square;
        }
        let ps = Math.pow(s, 2);
        let pw = Math.pow(W, 2);
        // console.log("maxvalue")
        // console.log(Math.max((rmx*pw)/ps, ps/(rmn*pw)))
        return Math.max((rmx * pw) / ps, ps / (rmn * pw))
      }

      // 将已经得到节点安置
      function layout(nodelist, value, x, y, direction, height, width, parent, leaves) {
        //比例尺
        let scale;
        //横向
        if (direction == 1)
          scale = d3.scaleLinear().domain([0, value]).range([0, width]);
        //纵向
        else scale = d3.scaleLinear().domain([0, value]).range([0, height]);
        let totValue = 0;
        for (let i = 0; i < nodelist.length; i++) {
          let node = nodelist[i]
          // 不存在叶节点
          if (node.children == null || node.children.length == 0) {
            let leaf = {
              name: node.name,
              value: node.value,
              x: direction == 1 ? x + scale(totValue) : x,
              y: direction == 1 ? y : y + scale(totValue),
              width: direction == 1 ? scale(node.square) : width,
              height: direction == 1 ? height : scale(node.square),
              parent: parent == -1 ? node.name : parent,
              square: node.square,
              children: []
            };
            leaves.push(leaf);
          }
          else
          // 存在叶节点，对节点进行递归计算
          {
            let x_ = direction == 1 ? x + scale(totValue) : x;
            let y_ = direction == 1 ? y : y + scale(totValue);
            let width_ = direction == 1 ? scale(node.square) : width;
            let height_ = direction == 1 ? height : scale(node.square);
            let parent_ = parent == -1 ? node.name : parent;
            let child = [];
            for (let i in node.children)
              child.push(node.children[i]);
            child.sort(function (a, b) { return b.square > a.square });
            let leaf = {
              name: node.name,
              value: node.value,
              x: direction == 1 ? x + scale(totValue) : x,
              y: direction == 1 ? y : y + scale(totValue),
              width: direction == 1 ? scale(node.square) : width,
              height: direction == 1 ? height : scale(node.square),
              parent: parent == -1 ? node.name : parent,
              square: node.square,
              children: []
            }
            calcPos(child, [], x_, y_, width_, height_, parent_, 100000000, leaf.children)
            leaves.push(leaf)
          }
          totValue += nodelist[i].square;
        }
      }

      // console.log(childlist.length);
      let direction = height < width ? 0 : 1;

      // 当前层全部计算完毕，将当前得到的结果直接安放
      if (childlist.length == 0) {
        let total = 0;
        for (let i = 0; i < rowlist.length; i++)
          total += rowlist[i].square;
        layout(rowlist, total, x, y, direction, height, width, parent, leaves);
      }
      // 对当前层的剩余节点进行计算
      else {
        let c = childlist[0];
        let newlist = [];
        for (let j = 0; j < rowlist.length; j++) {
          newlist.push(rowlist[j]);
        }
        newlist.push(c);
        // console.log(newlist);
        let w = Math.min(height, width);
        // console.log(w);
        // console.log("oldlist")
        // console.log(worst(rowlist, w))
        // console.log("newlist")
        // console.log(worst(newlist, w))
      
        let new_score = worst(newlist, w)
        // 在当前短边继续安放
        if (score >= new_score) {
          childlist.splice(0, 1);
          calcPos(childlist, newlist, x, y, width, height, parent, new_score, leaves);
        }
        else
        // 更换位置重新安放
        {
          let total = 0;
          for (let i = 0; i < rowlist.length; i++)
            total += rowlist[i].square;
          let height1 = direction == 1 ? total / width : height;
          let width1 = direction == 1 ? width : total / height;
          layout(rowlist, total, x, y, direction, height1, width1, parent, leaves);
          if (direction == 1)
            calcPos(childlist, [], x, y + height1, width, height - height1, parent, 100000000, leaves);
          else
            calcPos(childlist, [], x + width1, y, width - width1, height, parent, 100000000, leaves);
        }
      }
      return leaves
    }
  
    let childlist = [];
    for (let i in data.children)
      childlist.push(data.children[i]);
    childlist.sort(function (a, b) { return b.square > a.square });
    // console.log(childlist);
    let leaves = [];
    calcPos(childlist, [], 0, 0, width, height, -1, 100000000, leaves);
    return leaves;
  }


  // 显示图片
  function display(svg, d) {
    let leafa = treemap(d, width, height);
    console.log(leafa)
    svg.selectAll("g")
      .remove();
    
    // 绑定数据
    const leaf = svg
      .selectAll("g")
      .data(leafa)
      .join("g")
      .attr("transform", (d) => `translate(${d.x},${d.y})`);
    
    // 定义颜色模块
    let color = d3.scaleOrdinal(["dodgerBlue", "orange", "greenyellow", "tomato", "purple", "chocolate", "hotpink", "olive", "gold", "gray", "aqua", "violet", "yellow", "dimGray", "green", "indigo", "crimson", "royalblue"]);

    // console.log(svg);
    leaf
      .append("rect")
      .attr("id", (d) => d.name)
      .attr("stroke", "white")
      .attr("stroke-width", 1.5)
      .attr("fill", (d) => color(d.parent))
      .attr("fill-opacity",
        function (d) {
          var op = d.value;
          if (op > 400)
            op = 400;
          op = Math.sqrt(op) * 20;
          return op / 500 * 0.7 + 0.4
        })
      .attr("width", (d) => d.width)
      .attr("height", (d) => d.height);
    
    // 鼠标点击事件
    svg.selectAll("rect")
    .on("click", function (d, i) {
      display(svg, i);
    })
    
    // 鼠标悬停事件
    svg.selectAll("rect")
      .on("mouseover", function (d, i) {
        d3.select(this)
          .attr("fill", "white")
      })
      .on("mouseout", function (d, i) {
        d3.select(this)
          .transition()
          .duration(500)
          .attr("fill", (d) => color(d.parent))
          .attr("fill-opacity",
            function (d) {
              var op = d.value;
              if (op > 400)
                op = 400;
              op = Math.sqrt(op) * 20;
              return op / 500 * 0.7 + 0.4
            })
      })
    
    //文本设置
    leaf
      .append("text")
      .selectAll("tspan")
      .data((d) => (d.name + "|"+ d.square.toString()+ "|" +d.value.toString()).split(/(?=[A-Z][a-z])|\s+/g))
      .join("tspan")
      .attr("x", 3)
      .attr(
        "y",
        (d, i, nodes) => `${(i === nodes.length - 1) * 0.3 + 1.1 + i * 0.9}em`
      )
      .attr("fill-opacity", (d, i, nodes) =>
        i === nodes.length - 1 ? 0.7 : null
      )
      .attr("font-size",
        function (d) {
          console.log(d)
          let str = d.split("|");
          var v = parseInt(str[1]);
          v = Math.round(v / 10) + 5;
          if (v > 20)
            v = 20;
          return `${v}px`;
        })
      .text(function (d) {
        let str = d.split("|")
        return str[0]+str[2]
      });
    // console.log(leaf.select("rect"))
  }

  function main2() {
    d3.json(data_file).then(function (DATA) {
      setUi();
      data = DATA;
      display(d3.select("svg"), data)
    });
  }
}
