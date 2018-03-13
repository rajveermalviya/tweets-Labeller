importScripts('polyfill.js');
self.addEventListener('install', function(e) {

    e.waitUntil(caches.open('tweets-Labeller').then(function(cache) {

        return cache.addAll(['/', '/index.html', '/index.html?homescreen=1', '/?homescreen=1', ]);

    }));

});
