docker-compose exec luigi python -c \
  'from qgreenland.util.file import cleanup_output_dirs; cleanup_output_dirs()'
