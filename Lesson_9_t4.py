def fake_string(start_s, to_change_s, new_s, count_change) -> str:
    return start_s.replace(to_change_s, new_s, count_change)


print(fake_string('DC makes good movies, DC makes good comics', 'DC', 'Marvel', 1))
