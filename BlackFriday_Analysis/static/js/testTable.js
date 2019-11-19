
function testTable(){
    let tableLoc = "/testTable"

    d3.json(tableLoc).then(function(response){
        
        let tableData = response;

        // Get the reference to the table body
        let tbody = d3.select("tbody");


            // // Use Arrow Functions to build table 
            function buildTable(tableData){
                //Start by celaring existing data
                tbody.html("");
                // Loop thru data
                tableData.forEach(dataEntry => {
                    var row = tbody.append("tr");
                    Object.entries(dataEntry).forEach(([key, value]) => {
                    var cell = row.append("td");
                    cell.text(value);
                    });
                });
            }     
            

        buildTable(tableData);

    })
}

testTable();