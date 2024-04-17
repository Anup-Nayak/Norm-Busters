enemy_layout = import_csv_layout(level_data['Enemy'])
self.enemy = pygame.sprite.GroupSingle()
self.enemy_setup(enemy_layout)

def enemy_setup(self,layout):
for row_index,row in enumerate(layout):
for col_index,val in enumerate(row):
if val != -1:
x = col_index*TILESIZE
y = row_index*TILESIZE
if val == '0':
sprite = Enemy((x,y))
self.enemy.add(sprite)

    	self.enemy.update()

    	self.enemy.draw(self.display_surface)
