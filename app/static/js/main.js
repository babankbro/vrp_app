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
    } else {
        multiPointSelection.style.display = 'none';
        document.getElementById('textFieldContainer').innerHTML = ''; // Clear text fields if not multi
    }
}

function generateTextFields(numberOfFields) {
    const container = document.getElementById('textFieldContainer');
    container.innerHTML = ''; // Clear existing fields

    for (let i = 0; i < numberOfFields; i++) {
        const input = document.createElement('input');
        input.type = 'text';
        input.className = 'form-control';
        input.placeholder = `Point ${i + 1} Name`;
        input.name = `point${i + 1}`;
        input.id = `point${i + 1}`;
        container.appendChild(input);
    }
}