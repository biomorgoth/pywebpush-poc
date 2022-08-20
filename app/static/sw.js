'use strict';

self.addEventListener("push", (event) => {
    const title = event.data.text();
    console.log("A push message just came:", title);
    self.registration.showNotification(title);
}, false);
