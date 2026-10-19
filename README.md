# 奶龙唐笑字符画 API

根据用户提供的奶龙大笑、双手捧肚参考图制作的固定字符画接口。

## 公网调用

`GET https://nailong-tangxiao-api.vercel.app/api/nailong`

返回 UTF-8 `text/plain`，内容只包含 `art.txt` 中的字符画，允许跨域读取。

```powershell
curl.exe https://nailong-tangxiao-api.vercel.app/api/nailong
```

## 本地运行

```powershell
python server.py
curl.exe http://127.0.0.1:8000/api/nailong
```

无需第三方 Python 依赖。`api/nailong.py` 是 Vercel Python Function 入口；部署时需一并包含 `server.py` 和 `art.txt`。也可使用 Dockerfile 或 render.yaml。

## 接入 DeepSeek Harness（DSH）

在 Windows PowerShell 中，从本仓库根目录运行：

```powershell
$pluginDir = Join-Path $env:USERPROFILE '.dsh\plugins\nailong-api'
New-Item -ItemType Directory -Force $pluginDir | Out-Null
Copy-Item .\dsh-plugin\* $pluginDir -Force
dsh plugin --profile web add $pluginDir
dsh --profile web
```

然后让 DSH 调用 `nailong_tangxiao` 工具。插件默认访问上面的公网接口；网络请求失败时返回包内同一份字符画。可用环境变量 `NAILONG_API_URL` 覆盖地址。
