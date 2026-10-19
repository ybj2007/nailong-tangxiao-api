# 奶龙唐笑字符画 API

## 本地运行

无需安装 Python 依赖：

```powershell
python server.py
curl.exe http://127.0.0.1:8000/api/nailong
```

`GET /api/nailong`（以及 `GET /`）返回固定的 UTF-8 纯文本字符画。`--host` 可指定监听地址，`--port` 或环境变量 `PORT` 可指定端口。接口允许跨域读取。

## 部署成公网 API

此目录可直接作为单独的 Git 仓库。将它推送到 GitHub 后，在 Render 新建 Blueprint，选择该仓库并使用根目录的 `render.yaml`。部署成功后会得到 HTTPS 地址，例如：

```text
https://<你的服务名>.onrender.com/api/nailong
```

也可在其他支持 Docker 的平台使用此目录的 `Dockerfile`。容器监听 `0.0.0.0` 和平台提供的 `PORT`。部署完成后，先用浏览器或 `curl` 访问实际地址确认响应。

## 接入 DeepSeek Harness（DSH）

`dsh-plugin/` 是一个 DSH 工具插件，调用上面的公网 API 并向 DSH 提供 `nailong_tangxiao` 工具。先在运行 DSH 的环境中设置完整接口地址，再安装插件：

```powershell
$env:NAILONG_API_URL = 'https://<你的服务名>.onrender.com/api/nailong'
dsh plugin --profile web add ./dsh-plugin
dsh --profile web
```

如果以其他 profile 运行 DSH，请把两个命令中的 `web` 改成相应名称。设置环境变量后需重启 DSH 进程。然后可以在对话中要求它调用 `nailong_tangxiao`。也可以只使用公网 HTTP API，无须安装插件。
