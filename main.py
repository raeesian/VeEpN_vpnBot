import base64
import requests

def update_subscription():
    target_url = "https://erabinhood.ir/iran/config.php?sub"
    
    try:
        response = requests.get(target_url, timeout=15)
        raw_content = response.text.strip()
    except Exception as e:
        print(f"Error fetching source: {e}")
        return

    # بررسی Base64 بودن یا متن ساده
    is_base64 = False
    try:
        decoded_bytes = base64.b64decode(raw_content)
        decoded_text = decoded_bytes.decode('utf-8')
        is_base64 = True
    except Exception:
        decoded_text = raw_content

    lines = decoded_text.splitlines()
    modified_lines = []
    index = 1

    for line in lines:
        line = line.strip()
        if not line or line.startswith('//') or line.startswith('#'):
            continue

        new_name = f"t.me/VeEpN_vpnBot {index}"
        index += 1

        if '#' in line:
            base_config = line.split('#')[0]
            modified_line = f"{base_config}#{new_name}"
        else:
            modified_line = f"{line}#{new_name}"

        modified_lines.append(modified_line)

    final_text = "\n".join(modified_lines)

    if is_base64:
        final_output = base64.b64encode(final_text.encode('utf-8')).decode('utf-8')
    else:
        final_output = final_text

    # ذخیره خروجی نهایی در یک فایل
    with open("sub.txt", "w", encoding="utf-8") as f:
        f.write(final_output)

if __name__ == "__main__":
    update_subscription()
