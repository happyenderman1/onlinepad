const last = localStorage.getItem('notepad_doc')
const name = localStorage.getItem('notepad_doc_name')
document.getElementById('done-share').hidden = true
document.getElementById('change_name').hidden = true
document.getElementById('desc').hidden = true
document.getElementById('done').hidden = true 
function pass(){
	return ""
}
if (last == null){
	pass()
}
else{	
	document.getElementById('e').value = last
}
if (name == null){
	document.getElementById('name').innerText = "New file"
	localStorage.setItem('notepad_doc_name','New file')
}
else{
	document.getElementById('name').innerText = name
}
function cop(){
	const value = document.getElementById('e').value
	navigator.clipboard.writeText(value);
}
function copy_link(){
	let link = document.getElementById('link').textContent
	navigator.clipboard.writeText(link);
}
function save(filename, data) {
    const blob = new Blob([data], {type: 'text/txt'});
    if(window.navigator.msSaveOrOpenBlob) {
        window.navigator.msSaveBlob(blob, filename);
    }
    else{
        const elem = window.document.createElement('a');
        elem.href = window.URL.createObjectURL(blob);
        elem.download = filename;        
        document.body.appendChild(elem);
        elem.click();        
        document.body.removeChild(elem);
    }
}
function save(filename, data) {
    const blob = new Blob([data], {type: 'text/txt'});
    if(window.navigator.msSaveOrOpenBlob) {
        window.navigator.msSaveBlob(blob, filename + ".txt");
    }
    else{
        const elem = window.document.createElement('a');
        elem.href = window.URL.createObjectURL(blob);
        elem.download = filename + ".txt";        
        document.body.appendChild(elem);
        elem.click();        
        document.body.removeChild(elem);
    }
}
function download(){
	const value = document.getElementById('e').value 
	const name = localStorage.getItem('notepad_doc_name')
	save(name,value)
}
function newfile(){
	const verif = confirm("Are you sure want to delete this notes?")
	if (verif == true){
		document.getElementById('e').value = ""
		const value = document.getElementById('e').value 
		localStorage.setItem('notepad_doc',value)
		localStorage.setItem('notepad_doc_name','New file.txt')
		document.getElementById('name').innerText = "New file"
	}
	if (verif == false){
		return
	}
}
function publish(){
	let name = localStorage.getItem('notepad_doc_name')
	let value = document.getElementById('e').value
	$.post(`/api/v1/publish?name=${name}&text=${value}`,function (json) {
		document.getElementById('desc').hidden = false	
		document.getElementById('desc').innerText = `Your Public link is ${location.href}view?key=${json.key}`
		document.getElementById('done-share').hidden = false 
		document.getElementById('link').textContent = `${location.href}view?key=${json.key}`
		document.getElementById('link').hidden = true 
	}, 'json');
 
}
function fbshare(){
	let link = document.getElementById('link').textContent
	let ht = "https://"
	window.open(`${ht}www.facebook.com/sharer?u=${link}`)
}
function tweet(){
	let link = document.getElementById('link').textContent
	let a =  `https://twitter.com/intent/tweet?url=${location.href}&text=Hello,%20Make%20sure%20to%20check%20my%20cool%20note%20%F0%9F%94%A5!%0A%0A$%7Blink%7D%0A%0AOnlinePad%20:%20$%7Blocation.href%7D!"`
	window.open(a)
}
function savet(){
	const value = document.getElementById('e').value 
	localStorage.setItem('notepad_doc',value)
}
function change_name(){
	const new_name = document.getElementById('new_name').value 
	localStorage.setItem('notepad_doc_name',new_name)
	document.getElementById('change_name').hidden = true
	document.getElementById('desc').hidden = false
	document.getElementById('done').hidden = false
	document.getElementById('desc').innerHTML = `Changed Document name!`
	document.getElementById('name').innerText = new_name
}
function show_cn(){
	document.getElementById('change_name').hidden = false
	document.getElementById('new_name').value = "" 
}
function close_cn(){
	document.getElementById('change_name').hidden = true 
}
var close = document.getElementsByClassName("closebtn");
var i;

for (i = 0; i < close.length; i++) {
  close[i].onclick = function(){
		document.getElementById('done').hidden = true
  }
}
