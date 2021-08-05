from sqlalchemy.sql import text



class CRUDCaptcha:
    def get_captcha(session, id):
        try:
            query = text("""
                SELECT id, background_image, puzzle_piece_image, width, heigth, start_width, start_height, correct_width, correct_height, create_time, update_time 
                FROM captcha
                WHERE id=:id
                LIMIT 1
            """).params(id=id)
            record = session.execute(query).first()
            if record is None:
                raise Exception(f"captcha empty record")
            return record
        except Exception as e:
            raise Exception(f"captcha query error {e}")

    def get_list_ids(session):
        try:
            query = text("""
                SELECT id
                FROM captcha
            """).params(id=id)
            records = session.execute(query).all()
            captcha_ids = []
            for record in records:
                captcha_ids.append(record[0])
            return captcha_ids
        except Exception as e:
            raise Exception(f"captcha query error {e}")