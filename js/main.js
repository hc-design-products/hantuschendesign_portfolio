// =====Open Sidenav=====
(function ($) {
  ("use strict");

  // =====Dropdown=====

  // JavaScript to toggle the dropdown and modify overflow-y on #colorlib-aside
  const dropdownButton = document.querySelector(".dropdown-button");
  const dropdownContent = document.querySelector(".dropdown-content");
  const colorlibAside = document.querySelector("#colorlib-aside");
  // Toggle dropdown
  dropdownButton.addEventListener("click", function (event) {
    event.stopPropagation(); // Prevent the body click event from firing
    if (dropdownContent.style.display === "block") {
      dropdownContent.style.display = "none";
      colorlibAside.style.overflowY = "hidden"; // Disable overflow-y when dropdown is hidden
    } else {
      dropdownContent.style.display = "block";
      colorlibAside.style.overflowY = "auto"; // Enable overflow-y when dropdown is shown
    }
  });
  // Prevent dropdown from closing when clicking inside the dropdown content
  dropdownContent.addEventListener("click", function (event) {
    event.stopPropagation(); // Prevent clicks inside dropdown from closing it
  });

  // =====Burger Menu=====

  (function () {
    var lastScrollPosition = 0; // Variable to store the last scroll position of the aside
    $(".js-colorlib-nav-toggle").on("click", function (event) {
      event.preventDefault();
      var $this = $(this);
      if ($("body").hasClass("slideout")) {
        $this.removeClass("active");
        $("body").removeClass("slideout");
        setTimeout(function () {
          $("aside").scrollTop(0); // Set scroll position to 0
          dropdownContent.style.display = "none"; // Hide dropdown
          colorlibAside.style.overflowY = "hidden";
        }, 500); // Adjust the delay to match the slideout closing transition duration
      } else {
        $this.addClass("active");
        $("body").addClass("slideout");
        dropdownContent.style.display = "none"; // Hide dropdown
        colorlibAside.style.overflowY = "hidden"; // Disable overflow-y when dropdown is hidden
      }
    });
    // Ensure scroll position is 0 when slideout is removed by clicking outside
    $(document).click(function (e) {
      var container = $("#colorlib-aside, .js-colorlib-nav-toggle");
      if (!container.is(e.target) && container.has(e.target).length === 0) {
        if ($("body").hasClass("slideout")) {
          $("body").removeClass("slideout");
          $(".js-colorlib-nav-toggle").removeClass("active");
          setTimeout(function () {
            $("aside").scrollTop(0); // Set scroll position to 0
          }, 500); // Delay to match the slideout closing transition duration
        }
      }
    });
    $(window).scroll(function () {
      if ($("body").hasClass("slideout")) {
        $("body").removeClass("slideout");
        $(".js-colorlib-nav-toggle").removeClass("active");
        setTimeout(function () {
          $("aside").scrollTop(0); // Set scroll position to 0
        }, 500); // Delay to match the slideout closing transition duration
      }
    });
  })();
})(jQuery);

// =====PhotoFolio=====

document.addEventListener("DOMContentLoaded", () => {
  ("use strict");

  // =====Initiate glightbox=====

  const glightbox = GLightbox({
    selector: ".glightbox",
  });

  // =====Init swiper slider with 1 slide at once in desktop view=====

  new Swiper(".slides-1", {
    speed: 600,
    loop: true,
    autoplay: {
      delay: 5000,
      disableOnInteraction: false,
    },
    slidesPerView: "auto",
    pagination: {
      el: ".swiper-pagination",
      type: "bullets",
      clickable: true,
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
  });

  // =====Init swiper slider with 3 slides at once in desktop view=====

  new Swiper(".slides-3", {
    speed: 600,
    loop: true,
    autoplay: {
      delay: 5000,
      disableOnInteraction: false,
    },
    slidesPerView: "auto",
    pagination: {
      el: ".swiper-pagination",
      type: "bullets",
      clickable: true,
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
    breakpoints: {
      320: {
        slidesPerView: 1,
        spaceBetween: 40,
      },
      1200: {
        slidesPerView: 3,
      },
    },
  });
});

// =====Animation on scroll function and init=====

/*
function aos_init() {
  AOS.init({
    duration: 1000,
    easing: "ease-in-out",
    once: true,
    mirror: false,
  });
}
window.addEventListener("load", () => {
  aos_init();
});
*/

// =====Switch between G1 G2=====

$(document).ready(function () {
  // Set the default view (show gallery1 and hide gallery2)
  $("#gallery1").show();
  $("#gallery2").hide();
  // Function to handle link selection
  function selectLink(link) {
    $(".nav-g a").removeClass("selected-link"); // Remove the class from all links
    link.addClass("selected-link"); // Add the class to the selected link
  }
  // Add event listeners to the "switch to gallery" links
  $("#switchToGallery1").click(function (event) {
    event.preventDefault(); // Prevent the default link behavior
    $("#gallery2").fadeOut(300, function () {
      $("#gallery1").fadeIn(300);
      selectLink($("#switchToGallery1")); // Select the clicked link
    });
  });
  $("#switchToGallery2").click(function (event) {
    event.preventDefault(); // Prevent the default link behavior
    $("#gallery1").fadeOut(300, function () {
      $("#gallery2").fadeIn(300);
      selectLink($("#switchToGallery2")); // Select the clicked link
    });
  });
});

// =====Preloader new=====

const preloader = document.querySelector("#preloader");

// Image paths to preload
const imagePaths = [
  "../assets/image/Banners/banner1.webp",
  "../assets/image/Banners/banner2.webp",
  "../assets/image/Banners/banner3.webp",
  "../assets/image/Banners/banner4.webp",
  "../assets/image/Banners/banner5.webp",
];

// Preload Images with Promises
function preloadImages(paths) {
  return Promise.all(
    paths.map((path) => {
      return new Promise((resolve, reject) => {
        const img = new Image();
        img.src = path;
        img.onload = () => resolve(path); // Resolve when loaded
        img.onerror = () => reject(`Failed to load: ${path}`); // Handle errors
      });
    })
  );
}

// Preloader Logic
if (preloader) {
  window.addEventListener("load", () => {
    preloadImages(imagePaths) // Preload images first
      .then(() => {
        // Add the 'loaded' class after 1 second
        setTimeout(() => {
          preloader.classList.add("loaded");
        }, 1000);

        // Remove preloader and show content after 2 seconds
        setTimeout(() => {
          preloader.remove();
          document.getElementById("colorlib-main").style.opacity = 1;
        }, 2000);
      })
      .catch((error) => console.error(error)); // Log image load errors
  });
}

//===== auto add colorlib-active class to the current page=====

document.addEventListener("DOMContentLoaded", function () {
  const currentPath = window.location.pathname.split("/").pop();
  const navLinks = document.querySelectorAll("#colorlib-main-menu a");
  navLinks.forEach((link) => {
    if (link.getAttribute("href") === currentPath) {
      link.parentElement.classList.add("colorlib-active");
    }
  });
});

// =====lower the opacity of the language switcher after a delay=====

document.addEventListener("DOMContentLoaded", function () {
  const languageSwitcher = document.querySelector(".language-switcher");
  if (languageSwitcher) {
    // Lower the opacity after a delay
    setTimeout(function () {
      languageSwitcher.style.opacity = "0.7";
    }, 6000); // 3000ms = 3 seconds
    // Handle hover to restore opacity
    languageSwitcher.addEventListener("mouseenter", function () {
      languageSwitcher.style.opacity = "1";
    });
    languageSwitcher.addEventListener("mouseleave", function () {
      languageSwitcher.style.opacity = "0.7";
    });
  } else {
    console.error("Language switcher element not found");
  }
});
