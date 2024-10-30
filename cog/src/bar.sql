-- Outside cog

 SELECT *
  FROM custom_table;

-- [[[cog
-- import cog
--
-- for i in range(10):
--     fname = f"table_{i}"
--     cog.outl(f"select * from {fname};")
-- ]]]
--
-- [[[end]]]
