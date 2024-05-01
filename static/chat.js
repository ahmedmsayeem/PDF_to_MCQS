
    // Get a reference to the form
    const form = document.querySelector("form");

    // Add a submit event listener to the form
    form.addEventListener("submit", function(event) {
        // Prevent the default form submission behavior
        // event.preventDefault();

        // Get a reference to the .lds-roller element
        const ldsRoller = document.querySelector(".default");

        // Add the "default" class to the .lds-roller element
        ldsRoller.classList.add("lds-roller");
        ldsRoller.classList.remove("default");

        console.log("Form submitted. Adding .lds-roller. class to  'default'");
    });
