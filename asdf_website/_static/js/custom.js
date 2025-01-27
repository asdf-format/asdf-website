document.addEventListener('DOMContentLoaded', (event) => {
    const rtdAd = document.getElementById("readthedocs-ea");
    if (!rtdAd.hasAttribute("hidden")) {
        rtdAd.setAttribute("hidden", "true");
    }
});