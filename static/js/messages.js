/**
 * Automatically fades out and removes alert messages after 5 seconds.
 * 
 * This function waits for the DOM to fully load, then sets a timeout to:
 * 1. Select all elements with the class `.alert`.
 * 2. Apply a fade-out effect by setting `opacity` to `0` with a smooth transition.
 * 3. Remove the alert elements from the DOM after the transition completes.
 * 
 * The fade-out transition lasts 0.5 seconds.
 */
document.addEventListener("DOMContentLoaded", function () {
    setTimeout(function () {
        let alerts = document.querySelectorAll(".alert");
        alerts.forEach(alert => {
            alert.style.transition = "opacity 0.5s ease-in-out";
            alert.style.opacity = "0";
            setTimeout(() => alert.remove(), 500);
        });
    }, 5000);
});