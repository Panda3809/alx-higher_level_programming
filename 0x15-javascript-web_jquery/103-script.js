$(document).ready(function() {
  $('#btn_translate').click(translateHello);
  $('#language_code').keypress(function(event) {
    if (event.keyCode === 13) {
      translateHello();
    }
  });

  function translateHello() {
    const languageCode = $('#language_code').val();
    $.get(`https://www.fourtonfish.com/hellosalut/hello/${languageCode}`, function(data) {
      $('#hello').text(data.hello);
    });
  }
});
