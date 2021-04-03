document.addEventListener("DOMContentLoaded", function () {
    /**
     * HomePage - Help section
     */
    class Help {
        constructor($el) {
            this.$el = $el;
            this.$buttonsContainer = $el.querySelector(".help--buttons");
            this.$slidesContainers = $el.querySelectorAll(".help--slides");
            this.currentSlide = this.$buttonsContainer.querySelector(".active").parentElement.dataset.id;
            this.init();
        }

        init() {
            this.events();
        }

        events() {
            /**
             * Slide buttons
             */
            this.$buttonsContainer.addEventListener("click", e => {
                if (e.target.classList.contains("btn")) {
                    this.changeSlide(e);
                }
            });

            /**
             * Pagination buttons
             */
            this.$el.addEventListener("click", e => {
                if (e.target.classList.contains("btn") && e.target.parentElement.parentElement.classList.contains("help--slides-pagination")) {
                    this.changePage(e);
                }
            });
        }

        changeSlide(e) {
            e.preventDefault();
            const $btn = e.target;

            // Buttons Active class change
            [...this.$buttonsContainer.children].forEach(btn => btn.firstElementChild.classList.remove("active"));
            $btn.classList.add("active");

            // Current slide
            this.currentSlide = $btn.parentElement.dataset.id;

            // Slides active class change
            this.$slidesContainers.forEach(el => {
                el.classList.remove("active");

                if (el.dataset.id === this.currentSlide) {
                    el.classList.add("active");
                }
            });
        }

        /**
         * TODO: callback to page change event
         */
        changePage(e) {
            e.preventDefault();
            const page = e.target.dataset.page;

            console.log(page);
        }
    }

    const helpSection = document.querySelector(".help");
    if (helpSection !== null) {
        new Help(helpSection);
    }

    /**
     * Form Select
     */
    class FormSelect {
        constructor($el) {
            this.$el = $el;
            this.options = [...$el.children];
            this.init();
        }

        init() {
            this.createElements();
            this.addEvents();
            this.$el.parentElement.removeChild(this.$el);
        }

        createElements() {
            // Input for value
            this.valueInput = document.createElement("input");
            this.valueInput.type = "text";
            this.valueInput.name = this.$el.name;

            // Dropdown container
            this.dropdown = document.createElement("div");
            this.dropdown.classList.add("dropdown");

            // List container
            this.ul = document.createElement("ul");

            // All list options
            this.options.forEach((el, i) => {
                const li = document.createElement("li");
                li.dataset.value = el.value;
                li.innerText = el.innerText;

                if (i === 0) {
                    // First clickable option
                    this.current = document.createElement("div");
                    this.current.innerText = el.innerText;
                    this.dropdown.appendChild(this.current);
                    this.valueInput.value = el.value;
                    li.classList.add("selected");
                }

                this.ul.appendChild(li);
            });

            this.dropdown.appendChild(this.ul);
            this.dropdown.appendChild(this.valueInput);
            this.$el.parentElement.appendChild(this.dropdown);
        }

        addEvents() {
            this.dropdown.addEventListener("click", e => {
                const target = e.target;
                this.dropdown.classList.toggle("selecting");

                // Save new value only when clicked on li
                if (target.tagName === "LI") {
                    this.valueInput.value = target.dataset.value;
                    this.current.innerText = target.innerText;
                }
            });
        }
    }

    document.querySelectorAll(".form-group--dropdown select").forEach(el => {
        new FormSelect(el);
    });

    /**
     * Hide elements when clicked on document
     */
    document.addEventListener("click", function (e) {
        const target = e.target;
        const tagName = target.tagName;

        if (target.classList.contains("dropdown")) return false;

        if (tagName === "LI" && target.parentElement.parentElement.classList.contains("dropdown")) {
            return false;
        }

        if (tagName === "DIV" && target.parentElement.classList.contains("dropdown")) {
            return false;
        }

        document.querySelectorAll(".form-group--dropdown .dropdown").forEach(el => {
            el.classList.remove("selecting");
        });
    });

    /**
     * Switching between form steps
     */
    class FormSteps {
        constructor(form) {
            this.$form = form;
            this.$next = form.querySelectorAll(".next-step");
            this.$prev = form.querySelectorAll(".prev-step");
            this.$step = form.querySelector(".form--steps-counter span");
            this.currentStep = 1;

            this.$stepInstructions = form.querySelectorAll(".form--steps-instructions p");
            const $stepForms = form.querySelectorAll("form > div");
            this.slides = [...this.$stepInstructions, ...$stepForms];

            this.init();
        }

        /**
         * Init all methods
         */
        init() {
            this.events();
            this.updateForm();
        }

        /**
         * All events that are happening in form
         */
        events() {
            // Next step
            this.$next.forEach(btn => {
                btn.addEventListener("click", e => {
                    e.preventDefault();
                    this.currentStep++;
                    this.currentStep === 3 ? show_id() : null
                    this.currentStep === 5 ? make_summary() : null
                    this.updateForm();
                });
            });

            // Previous step
            this.$prev.forEach(btn => {
                btn.addEventListener("click", e => {
                    e.preventDefault();
                    this.currentStep--;
                    this.updateForm();
                });
            });

            // Form submit
            this.$form.querySelector("form").addEventListener("submit", e => this.submit(e));
        }

        /**
         * Update form front-end
         * Show next or previous section etc.
         */
        updateForm() {
            this.$step.innerText = this.currentStep;

            // TODO: Validation

            this.slides.forEach(slide => {
                slide.classList.remove("active");

                if (slide.dataset.step == this.currentStep) {
                    slide.classList.add("active");
                }
            });

            this.$stepInstructions[0].parentElement.parentElement.hidden = this.currentStep >= 6;
            this.$step.parentElement.hidden = this.currentStep >= 6;

            // TODO: get data from inputs and show them in summary
        }

        /**
         * Submit form
         *
         * TODO: validation, send data to server
         */
        submit(e) {
            // e.preventDefault();
            document.forms['donation_form'].submit();
            // this.currentStep++;
            // this.updateForm();
        }
    }

    const form = document.querySelector(".form--steps");
    if (form !== null) {
        new FormSteps(form);
    }

    /**
     * Functions for restApi in step 3
     */
    function show_id() {
        let ids = get_checked_chexboxes();
        let params = new URLSearchParams();
        ids.forEach(id => params.append("inst_ids", id))
        let address = '/get_inst_by_cat?' + params.toString();
        fetch(address)
            .then(response => response.text())
            .then(data => document.getElementById("institutions").innerHTML = data);
    }

    function get_checked_chexboxes() {
        let markedCheckbox = document.querySelectorAll('input[type="checkbox"]:checked');
        let ids = [];
        markedCheckbox.forEach(box => ids.push(box.value));
        console.log(ids);
        return ids;
    }

    function make_summary() {
        let bags = document.getElementById("id_quantity").value;
        let institution = document.querySelector('input[name="institution"]:checked').getAttribute('data-institution');
        let street = document.getElementById('id_address').value
        let city = document.getElementById('id_city').value
        let zip_code = document.getElementById('id_zip_code').value
        let phone_number = document.getElementById('id_phone_number').value
        let pick_up_date = document.getElementById('id_pick_up_date').value
        let pick_up_time = document.getElementById('id_pick_up_time').value
        let pick_up_comment = document.getElementById('id_pick_up_comment').value

        document.getElementById("summary_bags").innerHTML = bags + " worki zawierające";
        document.getElementById("summary_institution").innerHTML = 'Dla: ' + institution;

        let error = "<p style='color: darkred'>UZUPEŁNIJ DANE!</p>"

        let address = document.getElementById('summary_address')
        street !== "" ? address.firstElementChild.innerHTML = street : address.firstElementChild.innerHTML = error
        address.firstElementChild.nextElementSibling.innerHTML = city
        address.firstElementChild.nextElementSibling.nextElementSibling.innerHTML = zip_code
        address.lastElementChild.innerHTML = phone_number

        // street !== "" ? result === street : result === error
        // address.firstElementChild.innerHTML = result
        // city !== "" ? result === city : result === "<p style='color: darkred'>PODAJ MIASTO!</p>";
        // address.firstElementChild.nextElementSibling.innerHTML = result;
        // street !== "" ? result === street : result === "<p style='color: darkred'>PODAJ KOD!</p>";
        // address.firstElementChild.nextElementSibling.nextElementSibling.innerHTML = result;
        // street !== "" ? result === street : result === "<p style='color: darkred'>PODAJ NUMER TELEFONU!</p>";
        // address.lastElementChild.innerHTML = result;


        let date = document.getElementById('summary_date')
        date.firstElementChild.innerHTML = pick_up_date
        date.firstElementChild.nextElementSibling.innerHTML = pick_up_time
        date.lastElementChild.innerHTML = pick_up_comment
    }

    // document.querySelector('input[type=checkbox][name=is_taken]').onclick = function () {}
});
