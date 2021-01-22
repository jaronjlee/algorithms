Suppose a webpage contains a single text field. we want to make the page such that a user can immedietly start typing in the text field without clicking on it. what is correct way using HTML5?

https://stackoverflow.com/questions/45827/how-do-you-automatically-set-the-focus-to-a-textbox-when-a-web-page-loads

<input id="my-input" autofocus="autofocus" />
<script>
  if (!("autofocus" in document.createElement("input"))) {
    document.getElementById("my-input").focus();
  }
</script>

https://www.samanthaming.com/tidbits/42-html5-autofocus/
<input autofocus />

https://stackoverflow.com/questions/45827/how-do-you-automatically-set-the-focus-to-a-textbox-when-a-web-page-loads
<input type="text" name="myInput" autofocus />