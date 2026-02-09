document.addEventListener('DOMContentLoaded', function () {
  try {
    var imgs = document.querySelectorAll('article img');
    imgs.forEach(function (img) {
      if (img.closest('figure')) return;

      var alt = img.getAttribute('alt');
      // If image has no alt text, skip adding a caption
      if (!alt) return;

      var parent = img.parentNode;
      var wrapper = document.createElement('figure');
      wrapper.className = 'post-image';

      // If the image is wrapped in a link, move the link into the figure
      if (parent && parent.tagName && parent.tagName.toLowerCase() === 'a') {
        parent.parentNode.replaceChild(wrapper, parent);
        wrapper.appendChild(parent);
      } else {
        parent.replaceChild(wrapper, img);
        wrapper.appendChild(img);
      }

      var caption = document.createElement('figcaption');
      caption.className = 'post-image-caption';
      caption.textContent = alt;
      wrapper.appendChild(caption);
    });
  } catch (e) {
    console.error('image-captions.js error:', e);
  }
});
