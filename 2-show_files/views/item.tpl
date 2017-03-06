<html>
<head>
  <link href="../front/vendors/bootstrap.min.css" rel="stylesheet">
</head>
<body>
  <div class="col-md-12">Current item: <span id="index">?</span></div>
  <div class="col-md-12">Total: <span id="total">?</span></div>
  <div class="col-md-8" id="text">Lorem ipsum lorem ipsum</div>
  <div class="col-md-4" id="image">Put an image here</div>
  <script src="../front/vendors/jquery-3.1.1.min.js"></script>
  <script src="../front/vendors/bootstrap.min.js"></script>  
  <script>
      $( "#total" ).load( "../meta/total" );
      $( "#index" ).load( "../meta/index" );
      $( "#text" ).load( "../meta/text" );
      $( "#image" ).load( "../meta/imgname" );
  </script>  
</body>
</html>
