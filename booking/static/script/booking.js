
var selectedService = null
var selectedDate = null
var selectedTime = null

function onClickCallback(d, t, id, hours_str) {
    const date = document.getElementById("id_time_0")
    const time = document.getElementById("id_time_1")
    
    date.value = d
    time.value = `${t}:00:00`

    selectedDate = date.value
    selectedTime = `${t}:00`

    // Color in the clicked element
    // Uncolor all others
    
    var hours = JSON.parse(hours_str)
    
    for (let i_d = 0; i_d < 7; i_d++) {
        for (i_h in hours) {
            i_id = `${i_d}_${hours[i_h]}`

            const elem = document.getElementById(i_id);
            elem.style.backgroundColor = '';
        }
      }

    // Color the element
    const elem = document.getElementById(id);
    elem.style.backgroundColor = 'rgb(255 255 255 / 76%)';
    updatePage();
}

function onTypeClickCallback(type, treatment_ids) {
    const service_selector = document.getElementById("id_service")
    
    service_selector.value = type

    for (idx in treatment_ids) {
        const elem1 = document.getElementById(`hover_mask_${treatment_ids[idx]}`);
        elem1.style.backgroundColor = 'rgb(255 255 255 / 0%)';

        const elem2 = document.getElementById(`checkmark_${treatment_ids[idx]}`);
        elem2.style.visibility = 'hidden';
    }

    const elem1 = document.getElementById(`hover_mask_${type}`);
    elem1.style.backgroundColor = '#ffffff3d';

    const elem2 = document.getElementById(`checkmark_${type}`);
    elem2.style.visibility = 'visible';
    
    selectedService = service_selector.options[service_selector.selectedIndex].text

    updatePage();
}

function updatePage() {
    var paragraph = document.getElementById("booking_feedback");

    if (selectedService !== null && selectedDate !== null && selectedTime !== null) {
        paragraph.innerHTML = `You selected the ${selectedService} treatment at ${selectedTime} on ${selectedDate}`;
    }

    if (selectedService !== null) {
        var time_blur = document.getElementById("selectTimeWrapperBlur");
        time_blur.style.visibility = 'hidden';
    }
}


