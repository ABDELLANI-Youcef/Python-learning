<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Countries</title>
</head>
<body>
  <h1>Hello in countries list</h1>
  <ul>

    % for c in countries:
      <li>
        {{c['name']}} - {{c['capital']}} - {{c['population']}}
      </li>
    % end

  </ul>
</body>
</html>