document.addEventListener('DOMContentLoaded', (event) => {
    const adIds = ["readthedocs-ea", "readthedocs-ea-text-footer"];
    adIds.forEach(element => {
        var rtdAd = document.getElementById(element);
        if (rtdAd != null && !rtdAd.hasAttribute("hidden")) {
            rtdAd.setAttribute("hidden", "true");
        }
    });
});