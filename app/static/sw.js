'use strict';

self.addEventListener("push", (event) => {
    console.log("A push message just came:", event);
}, false);