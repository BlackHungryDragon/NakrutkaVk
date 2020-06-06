import vk_api,random,time
from colorama import Fore
banner="""

      N N  N    V K   K
      N  N  N  V  K K
      N   N   N   K   K

     coder : Naruto Uzumaki

"""

token = "bbea0638bef0ffbf708689fcb10a4d349cc38c0bd456c74cc6aebf6f0c6013434343b9af6136ac39d2bb7"
print(Fore.WHITE+banner)
vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()
print(Fore.YELLOW+'  Меню функций . \n [1] Лайки .  [2] Подписки. \n ')
doings =int(input(' Опция :'))
if doings == 1:
   print(' \n [1].Фото         [2].Пост')
   twodoings=int(input(' номер:'))
   if twodoings == 2:
      user_id =int(input(' id пользователя/группы :'))
      id=int(input(' id поста:'))
      def post():
         vk.likes.add(type ="post",owner_id=user_id,item_id=id)
      post()
   elif twodoings == 1:
      user_id=int(input(' id пользователя:'))
      id=int(input(' id: '))
      def photo():
         vk.likes.add(type ="photo",owner_id=user_id,item_id=id)
      photo()
elif doings == 2:
   id=int(input(' id: '))
   vk.groups.join(group_id=group)
   print(group)
   print("\n Успешно")
