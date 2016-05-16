var $task = $('#task');

var $title = $('input[name="title"]');
var $description = $('input[name="description"]');
var $priority = $('input[name="priority"]');
var $status = $('input[name="status"]');


$task.submit(function(){
  console.log('created task');

  $.ajax({
    method: 'post',
    url: 'http://localhost:8000/api/tasks/',
    data: {
      title: $title.val(),
      description: $description.val(),
      priority: $priority.val(),
      status: $status.val()
    }
  });

  return false;
});

var $tasks = $('#tasks');

$.get('http://localhost:8000/api/tasks/', function(tasks){
  tasks.results.forEach(function(task) {
    console.log(task)
    var $li = $('<li>');
    $li.text(task.title);
	$li.appendTo($tasks);
})
})

// $.post('http://localhost:8000/api/tasks/')



// $.patch('http://localhost:8000/api/tasks/')
// $.delete('http://localhost:8000/api/tasks/')
