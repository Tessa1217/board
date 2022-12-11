var titleArray = [
  { title: "title1" },
  { title: "title2" },
  { title: "title3" },
];

document.addEventListener("DOMContentLoaded", () => {
  let template =
    "<div class='border border-secondary m-2'><p>${title}</p></div>";
  $.template("sampleTemplate", template);
});

function makeTemplate() {
  $.tmpl("sampleTemplate", titleArray).appendTo("#template-body");
}
