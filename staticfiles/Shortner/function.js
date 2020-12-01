// function copy_function() {
//     /* Get the text field */
//     var copyText = document.getElementById("myInput");
  
//     /* Select the text field */
//     copyText.select();
//     copyText.setSelectionRange(0, 99999); /*For mobile devices*/
  
//     /* Copy the text inside the text field */
//     document.execCommand("copy");
  
//     /* Alert the copied text */
//     // alert("Copied the text: " + copyText.value);
//     var tooltip = document.getElementById("myTooltip");
//     tooltip.innerHTML = "Copied: " + copyText.value;
//   }
//   function outFunc() {
//     var tooltip = document.getElementById("myTooltip");
//     tooltip.innerHTML = "Copy to clipboard";
//   }
function copy_Function() {
  var copyText = document.getElementById("myInput");
  copyText.select();
  copyText.setSelectionRange(0, 99999)
  document.execCommand("copy");
  // alert("Copied the text: " + copyText.value);
  var tooltip = document.getElementById("myTooltip");
  tooltip.innerHTML = "Copied: " + copyText.value;
}

function outFunc() {
  var tooltip = document.getElementById("myTooltip");
  tooltip.innerHTML = "Copy to clipboard";
}


document.addEventListener('DOMContentLoaded', () => {

  //By default, submit button is disabled
  document.querySelector('#submit').disabled = true;


  document.querySelector('#task').onkeyup = () => {
      if(document.querySelector('#task').value.length > 0)
      {
      document.querySelector('#submit').disabled = false;
      }
      else{
          document.querySelector('#submit').disabled = true;
      }
  }

  
  
});


    

