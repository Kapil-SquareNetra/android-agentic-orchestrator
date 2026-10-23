# External tool setup guides

When the hub or a spoke asks the user to install or configure a tool, **include the matching section below** in the chat (or link to this file). Official docs stay the source of truth; these are quick paths for Android delivery.

---

## Figma MCP (Cursor)

**Docs:** [Cursor and Figma MCP](https://help.figma.com/hc/en-us/articles/39889260656407-Cursor-and-Figma-Set-up-the-MCP-server) · [Figma remote server](https://developers.figma.com/docs/figma-mcp-server/remote-server-installation/)

### Recommended — Figma plugin in Cursor

1. Open chat command palette (`Cmd Shift P` / `Ctrl Shift P`) → **Open chat**.
2. Run: `/add-plugin figma` → **Add Plugin**.
3. **Cursor Settings** → **Tools & MCP** → under Figma, click **Connect**.
4. In the browser, **Allow access** for your Figma account.

### Manual — remote server (no plugin)

1. **Cursor Settings** → **Tools & MCP** → add custom MCP server:

```json
{
  "mcpServers": {
    "figma": {
      "url": "https://mcp.figma.com/mcp"
    }
  }
}
```

2. Save → **Connect** next to Figma → sign in.

If remote OAuth fails on an older Cursor build, use the **desktop** server below.

### Fallback — Figma desktop MCP

1. Install/update the [Figma desktop app](https://www.figma.com/downloads/).
2. Open a Design file → **Dev Mode** (`Shift D`) → **Enable desktop MCP server** (runs at `http://127.0.0.1:3845/mcp`).
3. In Cursor **Tools & MCP**, add:

```json
{
  "mcpServers": {
    "figma-desktop": {
      "url": "http://127.0.0.1:3845/mcp"
    }
  }
}
```

**Verify:** In Agent chat, dynamic tools for Figma should list (e.g. `get_design_context`, `get_screenshot`). Paste a `figma.com/design/...?node-id=...` URL in the requirement when you want design compare at acceptance.

---

## Jira — MCP or Atlassian CLI (`acli`)

**Docs:** [Install ACLI](https://developer.atlassian.com/cloud/acli/guides/install-acli/) · [Get started with ACLI](https://developer.atlassian.com/cloud/acli/guides/how-to-get-started/)

Jira is optional. Use **either** a Jira/Atlassian MCP in Cursor **or** the CLI — not both required.

### Option A — Jira MCP in Cursor

1. **Cursor Settings** → **Tools & MCP** → add your org’s Jira MCP (or an Atlassian marketplace server your team uses).
2. Complete OAuth / API token steps in the server’s docs.
3. **Verify:** Issue fetch works from Agent chat with your issue key.

If no Jira MCP is available, use Option B.

### Option B — Atlassian CLI (macOS)

```bash
brew tap atlassian/homebrew-acli
brew install acli
acli --version
```

**Authenticate (pick one):**

```bash
# OAuth in browser (simplest)
acli jira auth login --web

# API token (create at id.atlassian.com → Security → API tokens)
echo "<YOUR_TOKEN>" | acli jira auth login \
  --site "your-site.atlassian.net" \
  --email "you@company.com" \
  --token
```

**Verify read access:**

```bash
acli jira workitem view AND-123
```

Replace `AND-123` with your issue key. Put the same key in the requirement **Jira** table.

---

## Detekt (Gradle, Android app module)

**Docs:** [Detekt Gradle setup](https://detekt.dev/docs/gettingstarted/gradle) · [Plugin portal](https://plugins.gradle.org/plugin/io.gitlab.arturbosch.detekt)

Detekt runs **inside the Android project**, not as a global install.

### Minimal setup (`:app` or feature module `build.gradle.kts`)

```kotlin
plugins {
    id("com.android.application")
    id("org.jetbrains.kotlin.android")
    id("io.gitlab.arturbosch.detekt") version "1.23.8"
}

detekt {
    buildUponDefaultConfig = true
    config.setFrom(files("$rootDir/config/detekt/detekt.yml"))
}
```

Use the latest stable version from the [plugin portal](https://plugins.gradle.org/plugin/io.gitlab.arturbosch.detekt) if `1.23.8` is outdated.

### Generate config and verify

```bash
cd /path/to/android-app
./gradlew detektGenerateConfig   # creates detekt.yml — move to config/detekt/ if you prefer
./gradlew tasks --all | grep detekt
./gradlew detekt
```

**Android note:** Apply the Detekt plugin on the **module** that holds Kotlin sources (usually `:app`), not only the root project.

**Existing codebase:** `./gradlew detektBaseline` creates a baseline to ignore legacy findings while you fix new code ([Detekt baselines](https://detekt.dev/docs/introduction/baseline/)).

If you skip Detekt, the orchestrator records **Detekt: N/A** and does not run the gate.

---

## Maestro CLI (+ device)

**Docs:** [Install Maestro CLI](https://docs.maestro.dev/maestro-cli/how-to-install-maestro-cli) · [Android](https://docs.maestro.dev/get-started/supported-platform/android)

### Prerequisites

- **Java 17+:** `java -version` (install OpenJDK 17+ if needed).
- **Android:** SDK platform tools (`adb`), emulator or USB device.

### Install CLI (macOS)

```bash
curl -fsSL "https://get.maestro.mobile.dev" | bash
maestro --version
```

**Homebrew alternative:**

```bash
brew tap mobile-dev-inc/tap
brew install mobile-dev-inc/tap/maestro
maestro --version
```

Open a **new terminal** after install so `maestro` is on `PATH`.

### Device / emulator

```bash
adb devices
# Start an AVD from Android Studio Device Manager, or connect a phone with USB debugging
maestro test --help
```

Read `applicationId` from `AndroidManifest.xml` for flows (`appId:` in YAML).

### Optional — Maestro MCP in Cursor

If your Cursor build exposes a **Maestro** MCP (e.g. `user-maestro`): **Settings → Tools & MCP** → enable it, then use `list_devices` before `run` / `inspect_screen`. The **CLI is enough** for `./gradlew` + `maestro test`; MCP is optional convenience.

**First flow smoke:**

```bash
cd /path/to/android-app
./gradlew :app:assembleDebug
maestro test .maestro/smoke.yaml
```

If you skip Maestro, the orchestrator records **Maestro: N/A** and does not run Maestro.

---

## Agent behavior

When offering setup:

1. Name the tool and whether it is **optional**.
2. Paste the **matching section** from this file (or summarize with the same steps and official links).
3. Ask: **Set up now**, **Already have it**, or **Skip (N/A for this feature)**.
4. Do not run installers or edit Gradle without explicit user approval.
