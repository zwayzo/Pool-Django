def reading_file():
    elements = []
    with open("periodic_table.txt", "r") as f:
        for line in f:
            name, attribute = line.split("=")
            attribute = attribute.strip(",")
            parts = attribute.split(",")
            data = {}
            for items in parts:
                key, value = items.split(":")
                data[key.strip()] = value.strip()
            element = {
                "name": name.strip(),
                "position": int(data["position"]),
                "number": data["number"],
                "symbol": data["small"],
                "mass": data["molar"],
                "electrons": data["electron"]
            }
            elements.append(element)

    rows = []
    current_row = [None] * 18
    last_position = 0
    for el in elements:
        pos = el["position"]
        # print(pos)
        if pos < last_position:
            rows.append(current_row)
            current_row = [None] * 18
        current_row[pos] = el
        last_position = pos
    rows.append(current_row)  

    # Write HTML
        # Write HTML
    with open("periodic_table.html", "w") as f:
        f.write("<!DOCTYPE html>\n")
        f.write("<html lang=\"en\">\n")
        f.write("<head>\n")
        f.write("  <meta charset=\"UTF-8\">\n")
        f.write("  <title>Periodic Table</title>\n")
        f.write("  <style>table { border-collapse: collapse; } td { border: 1px solid #333; padding: 10px; }</style>\n")
        f.write("</head>\n")
        f.write("<body>\n")
        f.write("<table>\n")
        for row in rows:
            f.write("  <tr>\n")
            for el in row:
                if el is None:
                    f.write("    <td style='background:#f0f0f0'></td>\n")
                else:
                    f.write("    <td>\n")
                    f.write(f"      <h4>{el['name']}</h4>\n")
                    f.write("      <ul>\n")
                    f.write(f"        <li>No {el['number']}</li>\n")
                    f.write(f"        <li>{el['symbol']}</li>\n")
                    f.write(f"        <li>{el['mass']}</li>\n")
                    f.write(f"        <li>{el['electrons']} electrons</li>\n")
                    f.write("      </ul>\n")
                    f.write("    </td>\n")
            f.write("  </tr>\n")
        f.write("</table>\n</body></html>\n")
    return elements

if __name__ == "__main__":
    elements = reading_file()