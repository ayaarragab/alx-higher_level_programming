const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';

$.get(url, function(data) {
  const characterName = data.name;
  $('#character').text(characterName);
});
