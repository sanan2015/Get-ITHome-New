from lib import cmd
from lib import html
from lib import paths
from lib import json

def main():
	cmd.title("IT之家最近更新")
	# cmd.size(66,36)
	try:
		soups = html.soup(html.getsoup("http://wap.ithome.com/").find_all("ul",attrs={"id": "wapindexnewlist"})).find_all("li")
		jsondata = json.data()
		jsondata = []
		for soup in soups:
			if len(soup.find_all("span",attrs={"class": "title"})) > 0:
				link = json.data()
				s = str(soup.find_all("span",attrs={"class": "title"})[0])
				link["title"] = s[s.rfind("\">")+3:s.rfind("</")]
				s = str(soup.find_all("span",attrs={"class": "date"})[0])
				link["time"] = s[s.rfind("('")+2:s.rfind("')")]
				link["link"] = "http://www.ithome.com" + soup.find_all("a")[0].attrs["href"]
				jsondata.append(link)
		print(json.dumps(jsondata).replace("	","    "))
		json.savefile(jsondata,paths.startpath() + "/Save.json")
	except Exception as e:
		print(e)
	cmd.pause("执行完成，按任意键继续...")
if __name__=='__main__':
	main()