function myFunction() {
  // Declare variables
  var input, filter, ul, li, a, i, txtValue;
  input = document.getElementById('myInput');
  filter = input.value.toUpperCase();
  list = document.getElementById("list");
  spans = list.getElementsByTagName('span');

  // Loop through all list items, and hide those who don't match the search query
  for (i = 0; i < spans.length; i++) {
    a = spans[i].getElementsByTagName("a")[0];
    txtValue = a.textContent || a.innerText;
    if (txtValue.toUpperCase().indexOf(filter) > -1) {
      spans[i].style.display = "";
    } else {
      spans[i].style.display = "none";
    }
  }
}
