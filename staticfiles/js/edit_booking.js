document.addEventListener("DOMContentLoaded", function () {
    // Select all edit buttons
    const editButtons = document.querySelectorAll(".edit-booking-btn");

    // Loop through all edit buttons and add event listener
    editButtons.forEach(button => {
        button.addEventListener("click", function () {
            // Get booking data attributes from the button
            const bookingId = this.getAttribute("data-booking-id");
            const contactName = this.getAttribute("data-contact-name");
            const numberOfGuests = this.getAttribute("data-number-of-guests");
            const bookingDate = this.getAttribute("data-booking-date");
            const bookingHour = this.getAttribute("data-booking-hour");
            const bookingMinute = this.getAttribute("data-booking-minute");
            const specialRequest = this.getAttribute("data-special-request");

            // Set values in the modal form
            document.getElementById("editBookingId").value = bookingId;
            document.getElementById("editContactName").value = contactName;
            document.getElementById("editNumberOfGuests").value = numberOfGuests;
            document.getElementById("editBookingDate").value = bookingDate;
            document.getElementById("editHour").value = bookingHour;
            document.getElementById("editMinute").value = bookingMinute;
            document.getElementById("editSpecialRequest").value = specialRequest;

            // Show the modal
            const editModal = new bootstrap.Modal(document.getElementById("editBookingModal"));
            editModal.show();
        });
    });
});
