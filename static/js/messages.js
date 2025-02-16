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