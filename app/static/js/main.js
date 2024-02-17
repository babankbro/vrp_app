function selectDepotType(type) {
    const multiPointSelection = document.getElementById('multiPointSelection');
    const multiPointDropdown = document.getElementById('multiPointDropdown');

    if (type === 'multi') {
        multiPointDropdown.innerHTML = ''; // Clear previous options
        for (let i = 1; i <= 5; i++) {
            let option = new Option(`${i} Point${i > 1 ? 's' : ''}`, i);
            multiPointDropdown.add(option);
        }
        multiPointSelection.style.display = '';
        generateTextFields(1)
    } else {
        multiPointSelection.style.display = 'none';
        document.getElementById('textFieldContainer').innerHTML = ''; // Clear text fields if not multi
    }
}

function generateTextFields(numberOfFields) {
    const container = document.getElementById('textFieldContainer');
    container.innerHTML = ''; // Clear existing fields

    // Create a table element
    const table = document.createElement('table');
    table.className = 'table'; // Assuming Bootstrap for styling

    const thead = document.createElement('thead');
    const headerRow = thead.insertRow();

    var header_names = ["Start Point", "LAT", "LNG", "End Point", "LAT", "LNG"];
    for (let i = 0; i < header_names.length; i++) {
        // Header for "Field Number"
        const headerCellNumber = document.createElement('th');
        headerCellNumber.textContent = header_names[i];
        headerRow.appendChild(headerCellNumber);
    }
  

    // Append the header to the table
    table.appendChild(thead);
    console.log("complete")
    const tbody = document.createElement('tbody');

    for (let i = 0; i < numberOfFields; i++) {
        // Create a row for each field
        const row = tbody.insertRow();
        for (let j = 0; j < 6; j++){
            // Create the label cell
            if (j==0 || j == 3){
                const labelCell = row.insertCell();
                const label = document.createElement('label');
                label.htmlFor = `point${i + 1}`;
                label.textContent = `#${i + 1}:`;
                labelCell.appendChild(label);
            }

            // Create the input cell
            else if (j==1 || j == 4){
                const inputCell = row.insertCell();
                const input = document.createElement('input');
                input.type = 'text';
                input.className = 'form-control';
                input.placeholder = `lat`;
                input.name = `lat${i + 1}`;
                input.id = `lat${i + 1}`;
                inputCell.appendChild(input);
            }
            else{
                const inputCell = row.insertCell();
                const input = document.createElement('input');
                input.type = 'text';
                input.className = 'form-control';
                input.placeholder = `lng`;
                input.name = `lng${i + 1}`;
                input.id = `lng${i + 1}`;
                inputCell.appendChild(input);
            }
            
        }
    }
    table.appendChild(tbody);
    // Append the table to the container
    container.appendChild(table);
    console.log("complete end")
}
