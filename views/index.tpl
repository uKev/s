<!DOCTYPE html> 
    <html> 
        <head> 
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"> 
            <title>The s URL-Shortener</title> 
            <style type="text/css"> 
              html {background-color: #eee; font-family: sans;}
              body {background-color: #fff; border: 1px solid #ddd; padding: 15px; margin: 15px;}
              pre {background-color: #eee; border: 1px solid #ddd; padding: 5px;}
            </style> 
            <link rel="shortcut icon" href="/static/favicon.ico"> 
        </head> 
        <body> 
            <h1>Hello, Welcome to the great, small and fast URL-Shortener <i>s</i></h1> 
            <p><strong>Warning:</strong> <i>s</i> is highly experimental. Use it only for non important stuff. It might eat your pets and children.</p> 
            <p>Enter the URL you want to be shorter:</p>
            <form method="post" >
            	<input type="text" action="/" size=150 name="url" value="http://" autofocus></input><br>
            	<small><i>Note: URL has to start with protocol, e.g. http://</small></i><br>
            	<input type="submit"></input>
            </form>
        </body> 
    </html> 