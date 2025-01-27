function hideHomePageAds(){
    var rtdAd = document.getElementById(id="readthedocs-ea");
    if (!rtdAd.hasAttribute("hidden")) {
        rtdAd.setAttribute("hidden", "true");
    }
}
