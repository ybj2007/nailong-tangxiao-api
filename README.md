# 奶龙唐笑字符画 API

## 本地运行

无需安装 Python 依赖：

```powershell
python server.py
curl.exe http://127.0.0.1:8000/api/nailong
```

`GET /api/nailong`（以及 `GET /`）返回固定的 UTF-8 纯文本字符画。字符画按用户提供的奶龙大笑参考图在本地生成，保存在 `art.txt`，部署时需与 `server.py` 一同提供。`--host` 可指定监听地址，`--port` 或环境变量 `PORT` 可指定端口。接口允许跨域读取。

## 部署成公网 API（Vercel）

当前公开接口：

```text
https://nailong-tangxiao-api.vercel.app/api/nailong
```

项目使用 Vercel Hobby 方案部署。`api/nailong.py` 是 Vercel Python Function 的入口。如需重新部署，可在该目录运行 `vercel deploy --prod --scope nailong-tangxiao --project nailong-tangxiao-api`，或把代码推送到 GitHub 后关联仓库。

## 其他部署方式

此目录也可使用 Docker 或 Render。Render 新建 Blueprint 时，选择仓库并使用根目录的 `render.yaml`。部署成功后会得到 HTTPS 地址，例如：

```text
https://<你的服务名>.onrender.com/api/nailong
```

也可在其他支持 Docker 的平台使用此目录的 `Dockerfile`。容器监听 `0.0.0.0` 和平台提供的 `PORT`。部署完成后，先用浏览器或 `curl` 访问实际地址确认响应。

## 接入 DeepSeek Harness（DSH）

`dsh-plugin/` 是一个 DSH 工具插件，调用上面的公网 API 并向 DSH 提供 `nailong_tangxiao` 工具。插件默认使用当前公开接口。在 Windows PowerShell 中，把插件复制到 DSH 自己的无空格目录后安装：

```powershell
$pluginDir = Join-Path $env:USERPROFILE '.dsh\plugins\nailong-api'
New-Item -ItemType Directory -Force $pluginDir | Out-Null
Copy-Item .\dsh-plugin\* $pluginDir -Force
dsh plugin --profile web add $pluginDir
dsh --profile web
```

如果以其他 profile 运行 DSH，请把两个命令中的 `web` 改成相应名称。然后可以在对话中要求它调用 `nailong_tangxiao`。如需覆盖接口地址，设置环境变量 `NAILONG_API_URL` 并重启 DSH。公网请求失败时插件会返回随包附带的同一份字符画。也可以只使用公网 HTTP API，无须安装插件。
