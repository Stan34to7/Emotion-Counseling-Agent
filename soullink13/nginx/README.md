# Nginx 配置说明（与服务器一致）

本目录提供与服务器相同的 nginx 配置，用于在本地 Windows 上通过 **5000** 端口统一访问 HTTP 和 WebSocket（`/human_ws`），方便与服务器环境一致、后续更新统一。

**上传 / 图生 3D 出现 413**：Nginx 默认 `client_max_body_size` 仅约 1MB。请以仓库内 `conf.d/soullink.conf` 为准（当前为 **500m**），并同步到线上；若前面还有一层反代（例如宿主机映射到容器的端口），**每一层**都要放宽请求体限制。

---

## 一、配置文件在哪

- **站点配置**：`conf.d/soullink.conf`（本仓库内路径：`nginx/conf.d/soullink.conf`）
- 需要把该文件放到 **你本机 nginx 安装目录** 下，例如：
  - `C:\nginx\conf\conf.d\soullink.conf`
  - 或 `D:\Program Files\nginx-1.26.x\conf\conf.d\soullink.conf`

---

## 二、操作步骤（详细）

### 步骤 1：确认 nginx 安装目录

假设 nginx 解压或安装在：

```
C:\nginx\
├── conf\           ← 配置目录
│   ├── nginx.conf   ← 主配置文件
│   └── conf.d\     ← 需要存在，用于放站点配置
├── nginx.exe
└── ...
```

记下你的 `conf` 的完整路径，例如：`C:\nginx\conf`。

### 步骤 2：创建 conf.d 并放入 soullink.conf

1. 进入 nginx 的 `conf` 目录（如 `C:\nginx\conf`）。
2. 若没有 `conf.d` 文件夹，新建一个，名称为：`conf.d`。
3. 将本仓库中的 `nginx/conf.d/soullink.conf` 复制到该目录下，最终路径为：
   ```
   <你的 nginx 目录>\conf\conf.d\soullink.conf
   ```
   例如：`C:\nginx\conf\conf.d\soullink.conf`。

**soullink.conf 内容（与服务器一致）：**

```nginx
# Soullink 站点配置（与服务器一致）
server {
    listen 5000;
    server_name _;

    # HTTP 接口：转发到 Flask 5002
    location / {
        proxy_pass         http://127.0.0.1:5002;
        proxy_set_header   Host $host;
        proxy_set_header   X-Real-IP $remote_addr;
        proxy_set_header   X-Forwarded-For $proxy_add_x_forwarded_for;
    }

    # WebSocket 音频通道：转发到 10002
    location /human_ws {
        proxy_pass         http://127.0.0.1:10002;
        proxy_http_version 1.1;
        proxy_set_header   Upgrade $http_upgrade;
        proxy_set_header   Connection "upgrade";
        proxy_set_header   Host $host;
    }
}
```

- **listen 5000**：nginx 监听 5000，对外只暴露 5000。
- **location /**：所有普通 HTTP 请求转发到本机 Flask（5002）。
- **location /human_ws**：WebSocket 路径 `/human_ws` 转发到本机 10002（数字人音频服务）。

### 步骤 3：让主配置引入 conf.d

1. 用记事本或 VS Code 打开 **主配置文件**：  
   `<你的 nginx 目录>\conf\nginx.conf`  
   例如：`C:\nginx\conf\nginx.conf`。

2. 找到 **http { ... }** 块。大致结构类似：

   ```nginx
   http {
       # ... 一堆现有配置 ...
       sendfile        on;
       keepalive_timeout  65;
       # ...
   }
   ```

3. 在 **http 块内部**（通常放在末尾，`}` 之前）增加一行：

   ```nginx
   include conf.d/*.conf;
   ```

   **注意：**
   - 路径是相对 nginx 的 `conf` 目录的，所以写 `conf.d/*.conf` 即可（不要写 `C:\nginx\conf\conf.d\...`）。
   - 必须写在 `http { }` 的花括号里面，不要写到 `http` 外面。

4. 示例（仅作参考，你的文件可能略有不同）：

   **修改前：**
   ```nginx
   http {
       include       mime.types;
       default_type  application/octet-stream;
       sendfile        on;
       keepalive_timeout  65;
   }
   ```

   **修改后：**
   ```nginx
   http {
       include       mime.types;
       default_type  application/octet-stream;
       sendfile        on;
       keepalive_timeout  65;

       include conf.d/*.conf;
   }
   ```

5. 保存 `nginx.conf`。

### 步骤 4：检查配置并启动 nginx

1. 打开命令行，进入 nginx 所在目录，例如：
   ```cmd
   cd C:\nginx
   ```

2. 测试配置是否正确：
   ```cmd
   nginx -t
   ```
   若显示 `syntax is ok` 和 `test is successful` 即表示配置无误。

3. 启动 nginx：
   ```cmd
   start nginx
   ```
   或直接：
   ```cmd
   nginx
   ```

4. 若之后修改了 `soullink.conf` 或 `nginx.conf`，重载配置即可，无需关进程：
   ```cmd
   nginx -s reload
   ```

---

## 三、使用方式

1. 先启动后端：在项目根目录执行 `python main.py`（会起 5002、10002）。
2. 再启动 nginx（如上）。
3. 本机/局域网访问：**http://本机IP:5000/**，前端配置后端地址为 **http://本机IP:5000**，音频走 **5000/human_ws**，与服务器一致。

---

## 四、常见问题

- **nginx -t 报错找不到 conf.d**  
  确认 `conf.d` 目录在 `conf` 下，且路径拼写为 `conf.d`（带点），且 `include conf.d/*.conf;` 写在 `http { }` 内部。

- **5000 无法访问**  
  先确认 `python main.py` 已运行（5002、10002 已启动），再确认 nginx 已启动；防火墙是否放行 5000 端口。

- **音频没有 / human_ws 连不上**  
  确认 `soullink.conf` 里 `location /human_ws` 的 `proxy_pass` 为 `http://127.0.0.1:10002`，且后端 10002 已启动。
