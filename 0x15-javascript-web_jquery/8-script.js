const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';

$.get(url, function(data) {
  const movies = data.results;
  const ul = $('<ul id="list_movies"></ul>');

  movies.forEach(function(movie) {
    const title = movie.title;
    const li = $('<li></li>').text(title);
    ul.append(li);
  });

  $('body').append(ul);
});
