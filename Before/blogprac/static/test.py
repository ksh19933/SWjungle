# import datetime
# now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
# from pymongo import MongoClient
# client = MongoClient('localhost', 27017)
# db = client.dbmyblog

# date= '2021-09-26%2002:00:50'
# print(date[0])
# db_date = date[:10] + " " + date[13:]
# test = db.post.find_one({'posted_date':db_date})
# print(test)


#   // function update(){
#   //   let title = $('#title').val();
#   //   let text = $('#main_text').val();
#   //   let category = $('#category').val();
#   //   let date = "{{db_data.posted_date}}";
#   //   $.ajax({
#   //     type: "POST",
#   //     url: "/page/update",
#   //     data:{title_give:title, text_give:text, category_give: category, 'posted_date': date},
#   //     success: function(){
#   //       location.href='../'
#   //     }
#   //   })
#   // }

#   // function remove(){
#   //   let date = "{{db_data.posted_date}}";
#   //   $.ajax({
#   //     type: "POST",
#   //     url: "/page/delete",
#   //     data:{'posted_date': date},
#   //     success: function(){
#   //       location.href='../'
#   //     }
#   //   })
#   // }
#   function get_data(){
#     path = window.location.pathname
#     if(path != '/page'){
#       $.ajax({
#         type: 'GET',
#         url: path,
#         data: {},
#         success: function(){
#           $('#title').val(data['title']);
#           $('#main_text').val(data['text']);
#           $('#category').val(data['category']);
#           temp_html=` <p></p>
#                       <p>
#                         <button onclick=update() style="margin-right:5px;">수정</button>
#                         <button onclick=remove()>삭제</button>
#                       </p>
#           `
#           $('#buttons').append(temp_html);
#           temp_html = `<button onclick=save()>등록</button>`
#           $('#buttons').append(temp_html);
#         }
#       })
#     }
#   }