function hideAds() {
    const adIds = ["readthedocs-ea", "readthedocs-ea-text-footer"];
    adIds.forEach(element => {
        var rtdAd = document.getElementById(element);
        if (rtdAd != null && !rtdAd.hasAttribute("hidden")) {
            rtdAd.setAttribute("hidden", "true");
        }
    });
}

function waitForVariable(variableName, timeout=5000) {
    return new Promise((resolve, reject) => {
        const startTime = Date.now();
        const intervalId = setInterval(() => {
            if (typeof window[variableName] != 'undefined') {
                clearInterval(intervalId);
                resolve(window[variableName]);
            } else if (Date.now() - startTime > timeout) {
                clearInterval(intervalId);
                reject(new Error(`Timeout waiting for ${variableName}`));
            }
        }, 100); // check every 100ms
    });
}

waitForVariable('ethicalads')
  .then((value) => {
    console.log('Variable is defined:', value);
    // proceed
    hideAds();
  })
  .catch((error) => {
    console.error(error);
    // handle timeout or error
  }, 2000);


