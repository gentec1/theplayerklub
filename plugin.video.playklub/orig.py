exec("import re;import base64");exec((lambda p,y:(lambda o,b,f:re.sub(o,b,f))(r"([0-9a-f]+)",lambda m:p(m,y),base64.b64decode("MzIgMTk5LDJhLCBkNywgMTY3ICxjLCAzNiwgMjcsIGVhLCAxNmEsIDY1CjMyIDU4LDExOSwxMjksZWUsMTJmCjMyIGU0LCBiOQoxMGQgNTEgMzIgNTEsIDE4NQozMiAxNDAsIDExNgo1OSA9ICc4OS5iMC4yYycKNTcgPSAzNi41Nyg1OSkKZTUgPSAzNi41Nyg3Yj0nODkuYjAuMmMnKQoxOWUgPSAiYmE9PSIKMzA9MTY3LjFiKDI1KGQ3LmJbMV0pLCAnMzAnKQozMz0xNjcuMWIoMjUoZDcuYlsxXSksICczMycpCjg1PTE2Ny4xYigyNShkNy5iWzFdKSwgJzEyMScpCmMwPTE2Ny4xYigyNShkNy5iWzFdKSwgJzgxJykKNjA9MTY3LjFiKDI1KGQ3LmJbMV0pLCAnZWQnKQo1ZSA9ICI1MjovL2NhLjE4Ni45YTphNS8xNDEuY2I/NDM9JThiJjUzPSU4YiY0Yj0xODAmOGM9MTdkIiUoMzAsMzMsKQo3NSA9ICI1MjovL2NhLjE4Ni45YTphNS9mYi5jYj80Mz0lOGImNTM9JThiIiUoMzAsMzMsKQoxMDcgPSA1Ny5kZCgnODAnKS5kYigiZjgtOCIpCmU9MjcuNjIoZWEuODAuMTA4KCdiNzovLzE3NScsJzEzMScsNTksJ2ZlLycpKTsKM2IgPSBlYS44MC4xMDgoMjcuNjIoImI3Oi8vMTAzL2Y0IiApLmRiKCJmOC04IiksIDU5KQo0ZiBmNyBlYS44MC4xNDkoM2IpOgoJZWEuMTA5KDNiKQoJCjE4IDMxKDE5MCk6Cgk1ZCA9IDJhLjc0KDE5MCkKCTVkLjU1KCdkMC1hOCcsICc4MScpCgkyZiA9IDJhLjc5KDVkKQoJMTliPTJmLmMyKCkKCTJmLjgyKCkKCTQ5IDE5YgoxOCBhNCg3NSk6CgkJNWQgPSAyYS43NCgxOTApCgkJIzVkLjU1KCdkMC1hOCcgLCAiMTUwIDEyNCIpCgkJNWQuNTUoJ2QwLWE4JywgJzEyMC81LjAgKDExZCAxOTEgNi4xOyAxOTg6MTEuMCkgMTUzLzEwMiAxMmQvMTEuMCcpCgkJMmYgPSAyYS43OSg1ZCkKCQkxOWI9MmYuYzIoKQoJCTJmLjgyKCkKCQk0OSAxOWIJCQoxOCBhMigpOgoJCTIzKCcxNjggYmUnLDc1LDEsZSArICczNC4yNCcpCgkJMjMoJzEwNCAxNmQnLCcxOTAnLDIsZSArICcxMDQgMTZkLjI0JykKCQkyMygnNjknLCc2OScsOCxlICsgJzE0Yi4yNCcpCgkJMjMoJzczICgxMzggMTY5KScsJzExYycsOSxlICsgJzExYS4yNCcpCgkJMjMoJ2RjJywnZGMnLDUsZSArICcxNDQuMjQnKQoJCTIzKCdhNiBiMicsJ2E2IGIyJyw3LGUgKyAnMTRmLjI0JykKCQkyMygnYTMnLCc5ZicsNCxlICsgJzlmLjI0JykKMTggZDUoMTkwKToKCWEwID0gNTguOWUoNWUpCgkzNyAzYSA0MSBhMDoKCQkxN2UgPSA1OC41NCgzYVsiNmYiXSkKCQkyMygxN2UgLDNhWyIxOTAiXSwgMywgNWYsIDIwPWFlKQoxOCA2YygxOTApOgoJCTE5YiA9IGE0KDE5MCkKCQkxZT02NS4xNignIjQzIjoiKC4rPykiJykuMTBlKDE5YikKCQljZj02NS4xNignIjE0YyI6IiguKz8pIicpLjEwZSgxOWIpCgkJOTE9NjUuMTYoJyIxMDYiOiIoLis/KSInKS4xMGUoMTliKSAJCgkJZDI9NjUuMTYoJyJkZiI6IiguKz8pIicpLjEwZSgxOWIpCgkJOTA9NjUuMTYoJyJmMCI6IiguKz8pIicpLjEwZSgxOWIpCgkJY2Q9NjUuMTYoJyJiMSI6IiguKz8pIicpLjEwZSgxOWIpCgkJZDE9NjUuMTYoJyIxMTciOiIxIicpLjEwZSgxOWIpCgkJMzcgMTkwIDQxIDFlOgoJCQkJMTlhKCcxNjggYmUgZGUnLCcnLCcnLGUgKyczNC4yNCcpCgkJCQkxOWEoJzMwOiAgJThiJyUoMTkwKSwnJywnJyxlICsgJzM0LjI0JykKCQkzNyAxOTAgNDEgY2Y6CgkJCQkxOWEoJzEzNzogICU4YiclKDE5MCksJycsJycsZSArICczNC4yNCcpCgkJMzcgMTkwIDQxIDkwOgoJCQkJZDMgPSA1MS42NChmNig5MFswXSkpCgkJCQlkMy45ZCgnJTE4OS0lMTk0LSVkICUxOTY6JTE5MzolMThlJykKCQkJCTE5YSgnMTFiOiAgJThiJyUoZDMpLCcnLCcnLGUgKyczNC4yNCcpCgkJMzcgMTkwIDQxIDkxOgoJCQkJZDMgPSA1MS42NChmNig5MVswXSkpCgkJCQlkMy45ZCgnJTE4OS0lMTk0LSVkICUxOTY6JTE5MzolMThlJykKCQkJCTE5YSgnMTE4OiAgJThiJyUoZDMpLCcnLCcnLGUgKyczNC4yNCcpCgkJMzcgMTkwIDQxIGQyOgoJCQkJMTlhKCcxNDUgODc6ICAlOGInJSgxOTApLCcnLCcnLGUgKyczNC4yNCcpCgkJMzcgMTkwIDQxIGNkOgoJCQkJMTlhKCcxN2MgODc6ICAlOGInJSgxOTApLCcnLCcnLGUgKyczNC4yNCcpIAoJCTM3IDE5MCA0MSBkMToKCQkJCTE5YSgnMTU2OiAxN2YnLCcnLCcnLGUgKyczNC4yNCcpCgkJIAoxOCBiZigxN2UsIDE5MCwgNWY9NTApOgoJCWM3PTE3ZQoJCWEwID0gNTguOWUoNWUpCgkJMzcgM2EgNDEgYTA6CgkJCTE3ZSA9IDU4LjU0KDNhWyI2ZiJdKQoJCQlkYT0zYVsiMTkwIl0KCQkJNGYgYzcgNDEgMTdlOgoJCQkJMWEgPSBjLjNmKDgwPWRhLCAxYz01ZikKCQkJCTFhLjRjKDRiPSI2NyIsIDI4PXsgIjY2IjogMTdlIH0pCgkJCQkxNjcuNWIoMjUoZDcuYlsxXSksIDQwLCAxYSkJCQkJCjE4IDE5YSgxN2UsMTkwLDE1OSw1Zik6CgkJMTAxPWQ3LmJbMF0rIj8xOTA9IisxOTkuZjIoMTkwKSsiJjE1OT0iK2FkKDE1OSkrIiYxN2U9IisxOTkuZjIoMTdlKQoJCTYxPTQwCgkJMmQ9Yy4zZigxN2UsIDRhPSI0NS4yNCIsIDFjPTVmKQoJCTJkLjRjKCA0Yj0iNjciLCAyOD17ICI2NiI6IDE3ZSB9ICkKCQk2MT0xNjcuMWQoNmQ9MjUoZDcuYlsxXSksMTkwPTEwMSwxYT0yZCwyMD1hZSkJCQkJCjE4IDIzKDE3ZSwgMTkwLCAxNTksIDVmLCA5ND0iIiwgMjA9NDAsIGU2PTUwKToKCTEwMT1kNy5iWzBdKyI/MTkwPSIrMTk5LmYyKDE5MCkrIiYxNTk9IithZCgxNTkpKyImMTdlPSIrMTk5LmYyKDE3ZSkrIiY1Zj0iKzE5OS5mMig1ZikrIiY5ND0iKzE5OS5mMig5NCkKCWE9ZDcuYlswXSsiPzE5MD01MCYxNTk9IithZCgxNTkpKyImMTdlPSIrMTk5LmYyKDE3ZSkrIiY1Zj0iKzE5OS5mMig1ZikrIiY5ND0iKzE5OS5mMig5NCkKCSMxNGQgMTdlLjE4YygnLVsxOGZdJywnJykuMThjKCctWzE5ZF0nLCcnKS4xOGMoJ1s0MiAxM2ZdJywnJykuMThjKCdbLzQyXScsJycpLjE4YygnICgxOWYpJywnJykrJz0nK2EKCTJkID0gYy4zZigxN2UsIDRhPTVmLCAxYz01ZikKCTJkLjRjKDRiPSI2NyIsIDI4PXsgIjY2IjogMTdlLCAiYzQiOiA5NH0pCgkyZC40ZSgnZjUnLCAnYTEnKQoJMTY3LjFkKDZkPTI1KGQ3LmJbMV0pLCAxOTA9MTAxLCAxYT0yZCwgMjA9MjApCjE4IDdmKCk6Cgk4NCA9IFtdCgk3MiA9IGQ3LmJbMl0KCTRmIGIzKDcyKSA+PSAyOgoJCTE4ZCA9IGQ3LmJbMl0KCQk2MyA9IDE4ZC4xOGMoJz8nLCcnKQoJCTRmICgxOGRbYjMoMThkKS0xXSA9PSAnLycpOgoJCQkxOGQgPSAxOGRbMDpiMygxOGQpLTJdCgkJNDggPSA2My5lMignJicpCgkJODQgPSB7fQoJCTM3IDE4YiA0MSAxNjAoYjMoNDgpKToKCQkJMjEgPSB7fQoJCQkyMSA9IDQ4WzE4Yl0uZTIoJz0nKQoJCQk0ZiAoYjMoMjEpKSA9PSAyOgoJCQkJODRbMjFbMF0uMTViKCldID0gMjFbMV0KCTQ5IDg0CgkKMTggN2QoKToKCgkyYyA9IDM2LjU3KCc4OS5iMC4yYycpCgk0NyA9IDJjLjFiKDdiPSczMCcpCgk0NiA9IDJjLjFiKDdiPSczMycpCgk4MyA9ICd7Ijc3IjoiMi4wIiwgIjhlIjoiYTMuYWIiLCAiMThkIjp7IjEyOCI6ImVjLjc2IiwgIjRkIjphMX0sIjdiIjoxfScKCWM4IAkgICA9ICd7Ijc3IjoiMi4wIiwiOGUiOiJkOS41NiIsIjE4ZCI6eyJiOCI6ImZjLjdlIiwiNzYiOmExfSwiN2IiOjF9JwoJOTcgICA9ICd7Ijc3IjoiMi4wIiwiOGUiOiJkOS41NiIsIjE4ZCI6eyJiOCI6ImZjLjE2NiIsIjc2IjphYX0sIjdiIjoxfScKCTk5ICAgPSAiNTI6Ly9jYS4xODYuOWE6YTUvMTQxLmNiPzQzPSIgKyA0NyArICImNTM9IiArIDQ2ICsgIiY0Yj05YiY4Yz0xNzIiCglkNAkgPSAiNTI6Ly9jYS4xODYuOWE6YTUvMTU4LmNiPzQzPSIgKyA0NyArICImNTM9IiArIDQ2ICsgIiY0Yj05YiY4Yz0xNzIiCgoJMjcuM2QoODMpCgkyNy4zZChjOCkKCTI3LjNkKDk3KQoJCgk2OCA9IDM2LjU3KCdmYy43ZScpCgk2OC4zZSg3Yj0nMTMzJywgNGQ9OTkpCgk2OC4zZSg3Yj0nMTNiJywgNGQ9ZDQpCgk2OC4zZSg3Yj0nMTE1JywgNGQ9ImFhIikKCTY4LjNlKDdiPScxMTMnLCA0ZD0iYWEiKQoJOGYgPSBjLjM5KCkuNjEoIls0MiBhOV1mZiAxNWQgMTc0Wy80Ml0iLCdbNDIgYTldMTljXCcxOTUgMTM1IDk4IDEyZSAxNmIgZTkgMTMyIGZmIDE1NFsvNDJdJywnICcsJ1s0MiBhOV0xNzYgMTBiIDEzMiAxODIgY2MgMTVlIDExNiBlOSAxMGMgMTc5IDE1YyAxMzkgZmZbLzQyXScpCgkKCjE4IDhhKCk6CgkyNy4xZignNWEoMTMwKScpCgkKMTggNmIoKToKCWU1LmM5KCkKCWEyKCkJCjE4IDcxKCk6Cgk4ZiA9IGMuMzkoKS4xNTIoJ2E2IDk4IGIyPycsICcxOGEgMTgzIDE1YSAxNzcgMTg0IDk4IDEyNSAxNWYgNjEgMTQzIDE2ZiAxMmIgOTggMTIyIDE3YSBmOScsIDEyYT0nMTNkJywxMTE9JzE5NycpCgk0ZiA4ZiA9PSAxOgoJCWU0LmViKCkKCjE4IGI1KDE3ZSwxOTAsMTU5LDVmLDE5ZSw5NCwyMj00MCxiND17fSk6CgkJMTAxPWQ3LmJbMF0rIj8xOTA9IisxOTkuZjIoMTkwKSsiJjE1OT0iK2FkKDE1OSkrIiYxN2U9IisxOTkuZjIoMTdlKSsiJjVmPSIrMTk5LmYyKDVmKSsiJjE5ZT0iKzE5OS5mMigxOWUpKyImOTQ9IisxOTkuZjIoOTQpCgkJNjE9NDAKCQkyZD1jLjNmKDE3ZSwgNGE9IjQ1LjI0IiwgMWM9NWYpCgkJMmQuNGMoIDRiPSI2NyIsIDI4PXsgIjY2IjogMTdlLCAiYzQiOiA5NCB9ICkKCQkyZC40ZSggIjcwIiwgMTllICkKCQk0ZiAyMjoKCQkJMzggPSBbXQoJCQk0ZiAyMiA9PSAnMTdiJzoKCQkJCTM4LmMzKCgnMTNhIDEwZCAnKzdjKycgOGQnLCcxMTAuOTIoJThiPzE1OT01JjE3ZT0lOGIpJwoJCQkJCQkJCQklKGQ3LmJbMF0sIDE5OS5mMigxN2UpKSkpCgkJCTRmIGY3IDE3ZSA0MSAxODE6CgkJCQkzOC5jMygoJzE3OCBlOSAnKzdjKycgOGQnLCcxMTAuOTIoJThiPzE1OT00JjE3ZT0lOGImMTkwPSU4YiY1Zj0lOGImMTE0PSU4YiknCgkJCQkJCSAlKGQ3LmJbMF0sIDE5OS5mMigxN2UpLCAxOTkuZjIoMTkwKSwgMTk5LmYyKDVmKSwgMTU5KSkpCgkJCTJkLjg4KDM4KQoJCTYxPTE2Ny4xZCg2ZD0yNShkNy5iWzFdKSwxOTA9MTAxLDFhPTJkLDIwPWFlKQoJCTQ5IDYxCgkJMTY3LjE0KDI1KGQ3LmJbMV0pKQoxOCBiYigxOTApOgoJMjcuMWYoJ2ZhKCU4YiknICUgMTkwKQoJMWEuOTYoNWYpCgkxNjcuNWIoMjUoZDcuYlsxXSksIDQwLCAxYSkKCQkKMTggYjYoMTllLDk0KToKCTRmIDg1ID09ICdhMSc6CgkJYzUgPSBjLjM5KCkuMTYzKCcxMGYnLCBiOS4xODcoNjAuMTQyKCdmOC04JykpLmZkKCksIDRiPWMuYmQsIDE0OD1jLmFjKQoJCTRmIGY3IGM1OgoJCQljLjM5KCkuNjEoJ2U4JywgJzExZiAzMycpCgkJODY6CgkJCTQ0ID0gMzEoJzUyOi8vMTg2LjlhL2Q4L2YzL2YzLjc4JykuMThjKCdcMTNjJywnJykuMThjKCdcMTUxJywnJykgICM3YQoJCQkxZSA9IDY1LjE2KCc8Mjk+KC4rPyk8LzI5PjwxOWI+KC4rPyk8LzE5Yj48MTQ2PiguKz8pPC8xNDY+PDE5ZT4oLis/KTwvMTllPicpLjEwZSg0NCkKCQkJMzcgMTdlLDE5MCw1ZiwxNyA0MSAxZToKCQkJCTRmICc3OCcgNDEgMTkwOgoJCQkJCWYoMTdlLDE5MCwxNSw1ZiwxNyw5NCkKCQkJCTg2OgoJCQkJCWYoMTdlLDE5MCwxMyw1ZiwxNyw5NCkKCTg2OgoJCWMuMzkoKS42MSgnZTgnLCAnMTU1IDExZSAxNmYgMTNlJykKCQkxNjcuMTQoMjUoZDcuYlsxXSkpCjE4IGYoMTdlLDE5MCwxNTksNWYsMTllLDk0LDIyPTQwLGI0PXt9KToKCQkxMDE9ZDcuYlswXSsiPzE5MD0iKzE5OS5mMigxOTApKyImMTU5PSIrYWQoMTU5KSsiJjE3ZT0iKzE5OS5mMigxN2UpKyImNWY9IisxOTkuZjIoNWYpKyImMTllPSIrMTk5LmYyKDE5ZSkrIiY5ND0iKzE5OS5mMig5NCkKCQk2MT00MAoJCTJkPWMuM2YoMTdlLCA0YT0iNDUuMjQiLCAxYz01ZikKCQkyZC40YyggNGI9IjY3IiwgMjg9eyAiNjYiOiAxN2UsICJjNCI6IDk0IH0gKQoJCTJkLjRlKCAiNzAiLCAxOWUgKQoJCTYxPTE2Ny4xZCg2ZD0yNShkNy5iWzFdKSwxOTA9MTAxLDFhPTJkLDIwPTQwKQoJCTQ5IDYxCgkJMTY3LjE0KDI1KGQ3LmJbMV0pKQoJCQoJCQoxOCA5MygxOWUsOTQpOgoJNDQgPSAzMSgnNTI6Ly8xODYuOWEvZDgvMTZlLjc4JykuMThjKCdcMTNjJywnJykuMThjKCdcMTUxJywnJykgICM3YQoJMWUgPSA2NS4xNignPDI5PiguKz8pPC8yOT48MTliPiguKz8pPC8xOWI+PDE0Nj4oLis/KTwvMTQ2PjwxOWU+KC4rPyk8LzE5ZT4nKS4xMGUoNDQpCgkzNyAxN2UsMTkwLDVmLDE3IDQxIDFlOgoJCTRmICc3OCcgNDEgMTkwOgoJCQlmKDE3ZSwxOTAsMTUsNWYsMTcsOTQpCgkJODY6CgkJCWYoMTdlLDE5MCwxMyw1ZiwxNyw5NCkKCTE2Ny4xNCgyNShkNy5iWzFdKSkKMTggNjkoMTllLDk0LDIyPTQwLCk6Cgk0NCA9IDMxKCc1MjovLzE4Ni45YS9kOC8xMDUuNzgnKS4xOGMoJ1wxM2MnLCcnKS4xOGMoJ1wxNTEnLCcnKSAgIzdhCgkxZSA9IDY1LjE2KCc8Mjk+KC4rPyk8LzI5PjwxOWI+KC4rPyk8LzE5Yj48MTQ2PiguKz8pPC8xNDY+PDE5ZT4oLis/KTwvMTllPicpLjEwZSg0NCkKCTM3IDE3ZSwxOTAsNWYsMTcsOTQgNDEgMWU6CgkJZigxN2UsMTkwLDEzLDVmLDE3LDk0KQoJCQoxOCBiYygxOTAsMTllLDk0KToKCTQ0ID0gMzEoMTkwKS4xOGMoJ1wxM2MnLCcnKS4xOGMoJ1wxNTEnLCcnKSAgIzdhCgkxZSA9IDY1LjE2KCc8Mjk+KC4rPyk8LzI5PjwxOWI+KC4rPyk8LzE5Yj48MTQ2PiguKz8pPC8xNDY+PDE5ZT4oLis/KTwvMTllPicpLjEwZSg0NCkKCTM3IDE3ZSwxOTAsNWYsMTcgNDEgMWU6CgkJNGYgJzc4JyA0MSAxOTA6CgkJCWYoMTdlLDE5MCwxNSw1ZiwxNyw5NCkKCQk4NjoKCQkJZigxN2UsMTkwLDEzLDVmLDE3LDk0KQoJMTY3LjE0KDI1KGQ3LmJbMV0pKQkKMTggMTI3KDE5MCk6CgkzNSA9IDE2YygxMmMsImEiKQoJMzUuMTYyKCcxNzA9IicrMTkwKyciXDEzYycpCgkzNS44MgoJYzY9MjcuMTRhKGMxKCkpCgkzMiBlMQoJNmU6IGM2LmM2KDE5MCkKCTNjOiA2YQoJMTY3LjE0KDI1KGQ3LmJbMV0pKQoJCjE4IDczKDE5ZSw5NCk6Cgk0NCA9IDMxKCc1MjovLzE4Ni45YS9kOC8xMDUuNzgnKS4xOGMoJ1wxM2MnLCcnKS4xOGMoJ1wxNTEnLCcnKSAgIzdhCgkxZSA9IDY1LjE2KCc8Mjk+KC4rPyk8LzI5PjwxOWI+KC4rPyk8LzE5Yj48MTQ2PiguKz8pPC8xNDY+PDE5ZT4oLis/KTwvMTllPicpLjEwZSg0NCkKCTM3IDE3ZSwxOTAsNWYsMTcgNDEgMWU6CgkJZigxN2UsMTkwLDEzLDVmLDE3LDk0KQoKMTggZTAoMTkwKToKCTJlKCkKCTZlOgoJCTVkID0gMmEuNzQoMTkwKQoJCWQ2ID0gMmEuNzkoNWQpCgkJOWMgPSBkNi5jMigpCgkJZDYuODIoKQoJCTE5KCkKCQk0ZiA5YyA9PSAnJzoKCQkJOWMgPSAnMTkyIDEyNiBlOSAxMjMsIGNjIDE0ZSAxNzMgZWYhJwoJCTQ5IDljCgkzYzoKCQkzMiBkNwoJCTMyIDVjIDE4OCAxNzEKCQkoZjEsIDRkLCA1YykgPSBkNy4xMTIoKQoJCTE3MS5hNyhmMSwgNGQsIDVjKQoJCTE5KCkKCQljZSA9IGMuMzkoKQoJCWNlLjYxKCJlNyEiLCJlNyBlMyBlOSAxMzYhIiwiIiwiMTQ3IDZlIDE2NSBlZi4iKQoKMTggMmUoKToKCTI3LjFmKCc1YShhZiknKQoKMTggMTkoKToKCTI3LjFmKCczOS4xNjEoYWYpJykKCTE2NCAyNy45NSgnMTM0LjEwYShhZiknKToKCQkyNy4xNTcoMTAwKQoKCQkKCgoxOGQ9N2YoKQoxOTA9NTAKMTdlPTUwCjE1OT01MAo1Zj01MAo5ND01MAoKNmU6MTkwID0gMTk5LjJiKDE4ZFsiMTkwIl0pCjNjOjZhCjZlOjE3ZSA9IDE5OS4yYigxOGRbIjE3ZSJdKQozYzo2YQo2ZTo1ZiA9IDE5OS4yYigxOGRbIjVmIl0pCjNjOjZhCjZlOjE1OSA9IDI1KDE4ZFsiMTU5Il0pCjNjOjZhCjZlOjk0PTE5OS4yYigxOGRbIjk0Il0pCjNjOjZhCgo0ZiAxNTkgPT0gNzoKCTcxKCkKMjYgMTU5ID09IDg6Cgk2OSgxOWUsOTQpCjI2IDE1OSA9PSA5OgoJNzMoMTllLDk0KQoyNiAxNTkgPT0gMToKCTZjKDE5MCkKMjYgMTU5ID09IDI6CglkNSgxOTApCjI2IDE1OSA9PSAzOgoJYmYoMTdlLCAxOTAsIDVmKQoyNiAxNTkgPT0gNDoKCTZiKCkKMjYgMTU5ID09IDU6Cgk5MygxOWUsOTQpCjI2IDE1OSA9PSA2OgoJYjUoMTdlLDE5MCw5NCkKMjYgMTU5ID09IDEwOgoJYjYoMTllLDk0KQoyNiAxNTkgPT0gMTE6Cgk3ZCgpCjI2IDE1OSA9PSAxNToKCWJjKDE5MCwxOWUsOTQpCjI2IDE1OSA9PSAxMjoKCThhKCkKMjYgMTU5ID09IDEzOgoJYmIoMTkwKQ==")))(lambda a,b:b[int("0x"+a.group(1),16)],"0|1|2|3|4|5|6|7|8|9|a|argv|xbmcgui|d|Images|addXMLMenu|10|11|12|13|endOfDirectory|15|compile|FanArt|def|mayfair_hide_busy_dialog|listitem|getSetting|thumbnailImage|addDirectoryItem|match|executebuiltin|isFolder|splitparams|showcontext|AddDir|png|int|elif|xbmc|infoLabels|title|urllib2|unquote_plus|playklub|liz|mayfair_show_busy_dialog|response|Username|OPEN_URL|import|Password|MyAcc|print_text_file|xbmcaddon|for|contextMenu|Dialog|channel|addon_data_dir|except|executeJSONRPC|setSetting|ListItem|True|in|COLOR|username|OPEN|DefaultFolder|password_text|username_text|pairsofparams|return|iconImage|type|setInfo|value|setProperty|if|None|datetime|http|password|GetEncodeString|add_header|SetAddonEnabled|Addon|common|AddonID|ActivateWindow|setResolvedUrl|traceback|req|ServerURL|iconimage|parental_pass|ok|translatePath|cleanedparams|fromtimestamp|re|Title|Video|moist|Movies|pass|OpenSettings|MyAccDetails|handle|try|display_name|Fanart_Image|Clear_Cache|paramstring|TVShows|Request|AccLink|enabled|jsonrpc|xml|urlopen|Spaf|id|ADDON_NAME|correctPVR|iptvsimple|Get_Params|path|vanemalukk|close|jsonSetPVR|param|show_adult|else|Connection|addContextMenuItems|plugin|LaunchPVR|s|output|Favorites|method|choice|match4|match2|RunPlugin|ExtraMenu|description|getCondVisibility|setThumbnailImage|nulldemo|your|loginurl|us|m3u_plus|data|strftime|m3u2list|settings|list|true|MainMenu|Settings|Open_URL|2095|Clear|print_exception|Agent|white|false|SetSettingValue|PASSWORD_VERIFY|str|False|10138|video|max_connections|Cache|len|allinfo|wizard2|wizard3|special|addonid|hashlib|ZmFuYXJ0LmpwZw|playXml|xmllist|INPUT_PASSWORD|Account|PlayUrl|Parental_Lock|GetPlayerCore|read|append|Plot|result|play|_NAME_|IPTVon|openSettings|dns|php|please|match5|dialog|match1|User|match6|match3|dt|EPGurl|LiveTv|reqq|sys|vod|Addons|stream|decode|Extras|getAddonInfo|Information|active_cons|gettextdata|urlresolver|split|connecting|GoDev|ADDON|background|Error|ERROR|to|os|Wipe_Cache|pvrmanager|vanemakood|downloader|later|created_at|etype|quote_plus|adult|addon_data|IsPlayable|float|not|utf|incorrect|PlayMedia|panel_api|pvr|hexdigest|resources|PVR|100|u|20100101|userdata|Live|vods|exp_date|addonDir|join|makedirs|IsActive|includes|populate|from|findall|Parental|XBMC|yeslabel|exc_info|epgCache|fav_mode|m3uCache|time|is_trial|Expires|xbmcvfs|tvshows|Created|TVshows|Windows|section|Invalid|Mozilla|showxxx|details|display|Browser|account|message|resolve|setting|zipfile|nolabel|clicked|watched|Firefox|Players|extract|TVGuide|addons|the|m3uUrl|Window|copied|server|Status|Coming|launch|Remove|epgUrl|n|Cancel|locked|yellow|base64|get|encode|button|extras|Active|thumbnail|Please|option|exists|Player|movies|status|print|check|cache|Magic|r|yesno|Gecko|Guide|Adult|Trial|sleep|xmltv|mode|still|lower|click|SETUP|allow|after|range|Close|write|input|while|again|demo|xbmcplugin|My|Soon|json|club|open|TV|main|is|item|tb|ts|back|DONE|home|This|cant|Add|now|are|fav|Max|hls|name|Yes|m3u|FAV|EPG|you|see|timedelta|theplayersklub|md5|as|Y|If|i|replace|params|S|US|url|NT|No|M|m|ve|H|OK|rv|urllib|AddAccInfo|link|We|EU|fanart|G".split("|")))