def sqr_cut(sqr,l_cut):
  print(f"def l_cut: {l_cut}")
  #cut 좌표 위치와 가로 좌표의 위치들을 비교하여 좌표를 반환한다. 이때 좌표 수의 크기는 sqr[0] < l_cut < sqr[1]
  return [sqr[0], l_cut],[l_cut, sqr[1]]

sqr_list = list(map(int, input().split()))
n_cut = int(input())
wids = [[0,sqr_list[0]]]
heis = [[0,sqr_list[1]]]

for _ in range(n_cut):
  seg, l_cut = list(map(int, input().split()))
  #axis의 정보를 임시 저장소에 담아두고, axis는 비워둔다.
  if seg == 1:
    temp_wid = list(wids)
    wids.clear()
    print(f"temp_wid: {temp_wid}")
    for j in range(len(temp_wid)):
      #cut 좌표의 위치를 확인하여 wid를 cut을 하는지 안하는지 확인
      if (l_cut > temp_wid[j][0]) & (l_cut < temp_wid[j][1]):
        #cut 함수 호출
        n_wid1, n_wid2 = sqr_cut(temp_wid[j], l_cut)
        wids.append(n_wid1)
        wids.append(n_wid2)
      else:
        wids.append(temp_wid[j])
  else:
    temp_hei = list(heis)
    print(f"temp_hei: {temp_hei}")
    heis.clear()
      #hei를 cut
    for j in range(len(temp_hei)):
      if (l_cut > temp_hei[j][0]) & (l_cut < temp_hei[j][1]):
        #cut 함수 호출
        n_hei1, n_hei2 = sqr_cut(temp_hei[j], l_cut)
        heis.append(n_hei1)
        heis.append(n_hei2)
      else:
        heis.append(temp_hei[j])
  print(f"wid: {wids}")
  print(f"hei: {heis}")

max = 0
for wid in wids:
  for hei in heis:
    area = (wid[1]-wid[0])*(hei[1]-hei[0])
    if area > max:
      max = area
print(max)
