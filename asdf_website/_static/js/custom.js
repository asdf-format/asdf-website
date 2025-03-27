function hideAds() {
    const adIds = ["readthedocs-ea", "readthedocs-ea-text-footer"];
    adIds.forEach(element => {
        var rtdAd = document.getElementById(element);
        if (rtdAd != null && !rtdAd.hasAttribute("hidden")) {
            rtdAd.setAttribute("hidden", "true");
        }
    });
}

if (document.readyState === "loading"){
    document.addEventListener('DOMContentLoaded', hideAds());
} else {
    hideAds();
}