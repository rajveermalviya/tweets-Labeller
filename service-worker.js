self.addEventListener('install', function(event) {
  event.waitUntil(
    caches.open('tweetLabeller').then(function(cache) {
      return cache.addAll(
        [
          '/index.html'
        ]
      );
    })
  );
})
document.querySelector('.cache-article').addEventListener('click', function(event) {
  event.preventDefault();
  var id = this.dataset.articleId;
  caches.open('tweetLabeller-' + id).then(function(cache) {
    fetch('/get-article-urls?id=' + id).then(function(response) {
      // /get-article-urls returns a JSON-encoded array of
      // resource URLs that a given article depends on
      return response.json();
    }).then(function(urls) {
      cache.addAll(urls);
    });
  });
});
self.addEventListener('fetch', function(event) {
  event.respondWith(
    caches.open('tweetLabeller').then(function(cache) {
      return cache.match(event.request).then(function (response) {
        return response || fetch(event.request).then(function(response) {
          cache.put(event.request, response.clone());
          return response;
        });
      });
    })
  );
});
