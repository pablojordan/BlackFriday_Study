function table() {
    ("#table2").dataTable({
        "iDisplayLength":10,
        "aLengthMenu": [[10,20, 50, 100,  -1], [10, 25, 50, 100, "All"]]
       });
      $("#table1").dataTable({
      "iDisplayLength":10,
      "aLengthMenu": [[10,20, 50, 100,  -1], [10, 25, 50, 100, "All"]]
      });
   };