window.addEventListener('load', () => {
    newPostBtn = document.getElementById('newpost-btn')
    newPostBtn.addEventListener('click', ()=>{
        document.getElementById('modal-container').style.display = 'flex';
        document.querySelector('.modal-title').innerText = 'New post'
        document.getElementById('modal-submit').onclick = ()=>{
            document.getElementById('modal-container').style.display = 'none';
            const data = new URLSearchParams();
            const text = document.getElementById('modal-textbox').value;
            data.append('text', text);
            fetch('/posts', {
                    method: 'post',
                    body: data
                }).then(res=>{
                    if (res.status == 200) {
                        location.reload()
                    }
                    else {
                        message = Object.assign(document.createElement('div'), {
                            className:'flash-message error',
                            innerText:'Failed to add post'
                           })
                       document.getElementById('flash-messages').appendChild(message)
                    }
                })
        }
        document.getElementById('modal-cancel').onclick = () => {
            document.getElementById('modal-container').style.display = 'none';
        }
    })
})

// window.addEventListener('load', () => {
//     newPostBtn = document.getElementById('newpost-btn')
//     newPostBtn.addEventListener('click', ()=>{
//         document.getElementById('modal-container').style.display = 'flex';
//         document.querySelector('.modal-title').innerText = 'New comment'
//         document.getElementById('modal-submit').onclick = ()=>{
//             document.getElementById('modal-container').style.display = 'none';
//             const data = new URLSearchParams();
//             const text = document.getElementById('modal-textbox').value;
//             data.append('text', text);
//             fetch('/posts', {
//                     method: 'post',
//                     body: data
//                 }).then(res=>{
//                     if (res.status == 200) {
//                         location.reload()
//                     }
//                     else {
//                         message = Object.assign(document.createElement('div'), {
//                             className:'flash-message error',
//                             innerText:'Failed to add post'
//                            })
//                        document.getElementById('flash-messages').appendChild(message)
//                     }
//                 })
//         }
//         document.getElementById('modal-cancel').onclick = () => {
//             document.getElementById('modal-container').style.display = 'none';
//         }
//     })
// })