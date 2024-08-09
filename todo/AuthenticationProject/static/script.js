const column = document.querySelector(".column");
const compose = document.querySelector(".compose");
const addNoteBtn = document.querySelector(".addNoteBtn");
const overlay = document.querySelector(".overlay");
const addNoteIcon = document.querySelector("#addNoteIcon");
const planBox = document.querySelector(".plan_box");
const removeBut = document.querySelector(".remove_but");
const menu = document.querySelector(".menu");
const profileTest = document.querySelector("#profileTest");
const arrow = document.querySelector(".arrow");

// column.addEventListener("mousemove", function () {
//   column.style.width = "250px";
//   compose.style.width = "90%";
//   addNoteBtn.classList.remove("hidden");
// });

// column.addEventListener("mouseleave", function () {
//   column.style.width = "80px";
//   addNoteBtn.classList.add("hidden");
//   compose.style.width = "50px";
// });

addNoteIcon.addEventListener("click", function () {
  overlay.classList.remove("hidden");
  planBox.classList.remove("hidden");
  // overlay.classList.add("hidden");
});

removeBut.addEventListener("click", function () {
  overlay.classList.add("hidden");
  planBox.classList.add("hidden");
});



document.querySelector('.arrow').addEventListener('click', function() {
  const menu = document.querySelector('.menu');
  menu.classList.toggle('hidden');
});

// Optional: Hide the menu when clicking outside of it
document.addEventListener('click', function(event) {
  const menu = document.querySelector('.menu');
  const arrow = document.querySelector('.arrow');
  
  if (!menu.contains(event.target) && !arrow.contains(event.target)) {
    menu.classList.add('hidden');
  }
});